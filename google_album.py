"""Gets a list of photos URLs from chosen Google Photos albums.
"""

import os

from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/photoslibrary.readonly']

SHARED_ALBUMS_TITLES = os.getenv('SHARED_ALBUMS_TITLES')
PAGE_SIZE = 100


def get_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8070)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def get_pics_urls_list():
    """Returns a list of URLs of pictures from the shared albums."""
    items_urls_list = []
    albums_id = []
    creds = get_credentials()
    try:
        service = build(
            'photoslibrary',
            'v1',
            credentials=creds,
            static_discovery=False,
            cache_discovery=False
        )
        albums_list = service.albums().list().execute().get('albums')
        for album in albums_list:
            if album['title'] in SHARED_ALBUMS_TITLES:
                albums_id.append(album['id'])

        for album_id in albums_id:
            searchbody = {
                'albumId': album_id,
                'pageSize': PAGE_SIZE
            }
            items_paginated = service.mediaItems().search(
                body=searchbody
            ).execute()

            items = items_paginated.get(
                'mediaItems'
            )

            for item in items:
                items_urls_list.append(item['baseUrl'])

            while 'nextPageToken' in items_paginated:
                searchbody = {
                    'albumId': album_id,
                    'pageSize': PAGE_SIZE,
                    'pageToken': items_paginated.get('nextPageToken')
                }

                items_paginated = service.mediaItems().search(
                    body=searchbody
                ).execute()

                items = items_paginated.get(
                    'mediaItems'
                )

                for item in items:
                    items_urls_list.append(item['baseUrl'])
    except HttpError as error:
        print(error)
    return items_urls_list


if __name__ == '__main__':
    print("Nested code only runs in the top-level code environment")

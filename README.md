# google_album_telegram_bot

telegram bot in python that allows you to share random photos from chosen google photos albums

## Installation 

Clone the repository 
    
    git clone git@github.com:alicezweig/google_album_telegram_bot.git

Create and activate virtual environment in project folder
    
     cd google_album_bot
     python -m venv venv 
     
   For Linux
   
     source venv/bin/activate
     
   For Windows
     
    venv/Scripts/activate
    
Install requred packages 
  
    python3 -m pip install --upgrade pip 

    pip install -r requirements.txt

## Setup

Create new Telegram bot and save the access token as `TELEGRAM_TOKEN` in `google_album_bot/.env`.

Input titles of Google Photos albums which you wish to share as they are to `SHARED_ALBUMS_TITLES` in `google_album_bot/.env`.

Example: `SHARED_ALBUMS_TITLES = ['My Lovely Cat', 'moreofmycat']`

Visit [https://developers.google.com/workspace/guides/create-credentials](https://developers.google.com/workspace/guides/create-credentials#oauth-client-id) to obtain OAuth client ID credentials. 

Save credentials as `google_album_bot/credentials.json`

## Run the application
  
    python3 bot.py
    
Enjoy random pictures of your cat in Telegram!
# Google Sheets API Tool

1. [Installation](#installation)
2. [Running](#running)
3. [Dependencies](#dependencies)

## Installation
Install all dependencies:
```
cd google_api_tool
pip install -e .
pip install -r requirements.txt
```
1. Open g_api_tool/config directory and change config.example.json to config.json
2. Create Google Workspace project and enable the API (https://developers.google.com/sheets/api/quickstart/python)
3. Create API Token of Google
4. Create Telegram Bot and get API Token of it, get chat id of yours
5. Fill out all data in config.json

## Running
```
cd google_api_tool/g_api_tool
python main.py
```

## Dependencies
1. Flask (Python library)
2. SQLAlchemy (Python library)
3. Google APIs libraries
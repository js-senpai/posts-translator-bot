import json

from dotenv import load_dotenv
import os
from os.path import join, dirname

# Initialize env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


# Base config
class BaseConfig:
    def __init__(self):
        pass

    def get_json_configs(self):
        with open('./settings.json', 'r') as file:
            # Read file
            get_data = file.read()
            return json.loads(get_data)
    TELEGRAM_API_TOKEN = os.environ.get('TELEGRAM_API_TOKEN', None)
    TELEGRAM_GROUP_FROM_IDS = os.environ.get('TELEGRAM_API_TOKEN', None)
    TELEGRAM_GROUP_TO_IDS = os.environ.get('TELEGRAM_GROUP_TO_IDS', None)
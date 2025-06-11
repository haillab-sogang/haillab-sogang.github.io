import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_PATH = os.path.join(BASE_PATH, 'docs')
API_KEY = os.getenv('INPUT_API_KEY', '') or 'AIzaSyA9_AkhjKlxNuPfapTJoR4FQRyYU_bKEvY'

DATA_URL = 'https://docs.google.com/spreadsheets/d/1d6JnxAHQg8DLUq7Jh4lB5dvcH8Exy7duHRTXK6MTf94'

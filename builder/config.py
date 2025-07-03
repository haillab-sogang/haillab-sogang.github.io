import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_PATH = os.path.join(BASE_PATH, 'docs')
API_KEY = os.getenv('INPUT_API_KEY', '') or 'AIzaSyANa2XqUvv27xKFyzpi55F4tuuX2PTr-Ys'

DATA_URL = 'https://docs.google.com/spreadsheets/d/1waiUmv5rEyhDjtq0aaPdEJ8KllI22kFexF8VWl5OYNg/'
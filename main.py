import os
import random

from flask import Flask, render_template
import requests
from dotenv import load_dotenv

load_dotenv()

STATUS = [
    'RISES',
    'SOARS',
    'SHOOTS UP',
    'SURGES',
    'HIKES',
    'SKYROCKETS',
    'TANKS',
    'PLUMMETS',
    'NOSEDIVES',
    'CRASHES',
    'PLUNGES',
    'SLUMPS',
]

URL = ('http://newsapi.org/v2/top-headlines?'
       'language=en&'
       f'apiKey={os.getenv("API_KEY")}')

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get(URL)
    articles = response.json()['articles']
    headline = random.choice(articles)['title'].upper()

    return render_template('index.html', status=random.choice(STATUS), headline=headline)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

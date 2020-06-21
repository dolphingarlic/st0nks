import os
import random

from flask import Flask, render_template
import requests

STATUS = [
    'RISES',
    'SOARS',
    'SHOOTS UP',
    'SURGES',
    'HIKES',
    'TANKS',
    'PLUMMETS',
    'NOSEDIVES',
    'CRASHES',
    'PLUNGES',
]

URL = ('http://newsapi.org/v2/top-headlines?'
       'language=en&'
       f'apiKey={os.environ["API_KEY"]}')

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get(URL)
    articles = response.json()['articles']
    headline = random.choice(articles)['title'].upper()

    return render_template('index.html', status=random.choice(STATUS), headline=headline)


if __name__ == '__main__':
    app.run()

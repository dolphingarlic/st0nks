import os
import random

from flask import Flask, render_template, Response
import requests
from dotenv import load_dotenv
import tweepy

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
CACHE = []
URL = ('http://newsapi.org/v2/top-headlines?'
       'language=en&'
       f'apiKey={os.getenv("NEWS_API_KEY")}')


def get_headline():
    global CACHE
    if len(CACHE) == 0:
        response = requests.get(URL)
        CACHE = response.json()['articles']
    article = random.choice(CACHE)
    CACHE.remove(article)
    return article['title'].upper()


app = Flask(__name__)


@app.route('/')
def home():
    headline = get_headline()
    return render_template('index.html', status=random.choice(STATUS), headline=headline)


tweepy_auth = tweepy.OAuthHandler(
    os.getenv('TWEEPY_API_KEY'), os.getenv('TWEEPY_API_SECRET_KEY'))
tweepy_auth.set_access_token(
    os.getenv('TWEEPY_ACCESS_TOKEN'), os.getenv('TWEEPY_ACCESS_TOKEN_SECRET'))

tweepy_api = tweepy.API(tweepy_auth)


@app.route('/tweet/')
def tweet():
    status = random.choice(STATUS)
    headline = get_headline()

    try:
        tweepy_api.verify_credentials()
        tweepy_api.update_status(
            f'St0nks Update:\n\nStock market {status} as {headline}' +
            '\n\n(This is for entertainment purposes only. ' +
            'This Tweet was sent automatically using st0nks.ml)')
        return Response(status=200)
    except:
        print('Couldn\'t Tweet :(')
        return Response(status=401)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

# twitter_client.py
import tweepy
from django.conf import settings

client = tweepy.Client(bearer_token=settings.TWITTER_BEARER_TOKEN)

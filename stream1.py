from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
access_token = '830795167724601344-Esd939k1LwRWmG8vzVRcW1XGqloc54t'
access_token_secret = 'XEZxlzH6hH055hXHEBn5yKcFFCZTPTPhaft7F2jgKYplt'
consumer_key = 'yuBo4oZM4kxi9iHiQpxPREBK7'
consumer_secret = 'aC5l5WlOcF4KRmGYXCX5HGkSUBjFapU2C4BiJRdrKGegwjkksF'

tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
auth.secure = True
api = tweepy.API(auth)

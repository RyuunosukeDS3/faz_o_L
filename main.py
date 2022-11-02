from tweepy import StreamRule

from api import TwitterManager
from config import Config

config = Config()
twitter_manager = TwitterManager(str(config.bearer_token))


def start_streaming():

    twitter_manager.add_rules(StreamRule("faz o l"))

    twitter_manager.filter(tweet_fields=["referenced_tweets", "author_id"])


start_streaming()

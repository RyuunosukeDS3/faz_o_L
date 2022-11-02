import os
import os.path
from random import randint
from time import sleep

import tweepy
from config import Config


class TwitterManager(tweepy.StreamingClient):
    config = Config()
    auth = tweepy.OAuth1UserHandler(
        str(config.api_key),
        str(config.api_key_secret),
    )
    auth.set_access_token(
        str(config.access_token),
        str(config.access_token_secret),
    )
    twitter = tweepy.API(auth)

    def on_connect(self):
        print("Connected")

    def on_tweet(self, tweet):
        try:
            for referenced_tweet in tweet.referenced_tweets:
                matches = ["faz", "o", "l"]
                if (
                    referenced_tweet["type"] == "replied_to"
                    and tweet.data["author_id"] != str(self.config.author_id)
                    and (word in tweet.text for word in matches),
                ):
                    max = 0
                    for _ in os.listdir("/workspace/images"):
                        max += 1
                    number = randint(1, max)
                    self.twitter.update_status_with_media(
                        filename=f"/workspace/images/lula_{number}.png",
                        status="",
                        in_reply_to_status_id=tweet.id,
                        auto_populate_reply_metadata=True,
                    )
                    print(tweet.data)
                    sleep(20)
        except Exception as err:
            print(err)

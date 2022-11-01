import tweepy


class TwitterManager:
    def __init__(self):
        auth = tweepy.OAuth1UserHandler("", "")
        auth.set_access_token("", "")
        self.twitter = tweepy.API(auth)

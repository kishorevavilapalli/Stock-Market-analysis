import tweepy
import json
import csv

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "2241962310-czk0fhewfm8VN1XoSSAZhOqZXtsMUOOp37i5mg8"
access_token_secret ="tCcTCJU3xj2mxEY3f41o8uKctu8NOYY6WNOO9IMtt3ELz"
consumer_key = "KYqNMPufDBAJPA9vb18G3ZZcZ"
consumer_secret ="MRBKvD1jUsrXTjbT8lxC7DKzwkXOFRfAUTOK2ACOlbLM5BYIUr"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        new_data = json.loads(data)
        tweet = new_data["text"].encode("utf-8")
        time = new_data["created_at"]
        user_id = new_data["user"]["id"]
        tweet_id = new_data["id"]

        with open("c:\Python27/BITCOIN.csv", "ab") as csvfile:
            myfile = csv.writer(csvfile)
            myfile.writerow([tweet,time,user_id,tweet_id])
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['#Bitcoin'])
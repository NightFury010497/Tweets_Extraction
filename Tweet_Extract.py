from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''



try:
    while True:
        class listener(StreamListener):
            def on_data(self, data):
                savefile=open('tweet.json','a')
                savefile.write(data)
                savefile.write('\n')
                savefile.close()
                return True
                print(data)
            def on_error(self, status):
                print(status)

        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=["#bitcoin"])
except KeyboardInterrupt:
    pass


import pandas as pd
df = pd.read_json (r'tweet.json', lines=True)
col = []
df2 = pd.DataFrame(columns=col)
df2['id'] = df['id']
df2['text']= df['text']
df2.dropna(axis=1, how='all')
df2.to_csv (r'Bitcoin.csv', index = None)





# Cannabis-Sentiment
Gauges legalization sentiment of illegal states using TextBlob for natural language processing of tweets from Twitter.

1. You will need to create your own google sheet of GDP's and set up a client_secret.json file if you want to filter by GDP. Instructions here: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
(Comment out lines 13 and 17 of main.py if you choose not to do this step)

2. Connect to the Twitter API, I used the tweepy module: https://stackabuse.com/accessing-the-twitter-api-with-python/

4. Put your twitter credentials in lines 15-19 of twitter_analysis.py

from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['weather', 'rain', 'rainy', 'raining', 'sunny', 'cloudy'
                      'foggy', 'fog', 'hail', 'hailing', 'snow.' 'snowing'], or_operator=True)
    tso.set_language('en')
    tso.set_geocode(42.3744, -71.1169, 5, True)
    tso.set_include_entities(False) # and don't give us all those entity information

    ts = TwitterSearch(
                       consumer_key = '0foq3ttMublojZmIuth76mzDP',
                       consumer_secret = '72t1Iaa4JOc60ZJb8UgejqcjIWK3g5OiJt2JnXXnNy2MbDuZ7K',
                       access_token = '4188038303-tlz5WruG6b78FugN2CBq9lsuRa5IJYtnzxgRMwr',
                       access_token_secret = 'bLLK8LDSyAVUL9EVtQkNGDHx8DP1FGRleNwi5FVqMrNVi'
                       )
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s at %s at %s' % ( tweet['user']['screen_name'], tweet['text'], tweet['geo'], tweet['created_at'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
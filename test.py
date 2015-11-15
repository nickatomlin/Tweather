from itertools import islice
import datetime
import operator
import re

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def weather_desc(tweets):
    notions = {'windy': 0.0,
               'comfortable': 0.0,
               'refreshing': 0.0,
               'beautiful': 0.0,
               'ominous': 0.0,
               'miserable': 0.0,
               'foggy': 0.0,
               'severe': 0.0,
               'humid': 0.0,
               'muggy': 0.0,
               'stormy': 0.0,
               'flooding': 0.0}
    temps = {'warm': 0.0,
             'hot': 0.0,
             'cold': 0.0,
             'freezing': 0.0}
    precs = {'clear': 0.0,
             'overcast': 0.0,
             'raining': 0.0,
             'sunny': 0.0,
             'hailing': 0.0,
             'snowing': 0.0,
             'foggy': 0.0,
             'cloudy': 0.0}

    texts = []
    tweeters = []

    for tweet in tweets:
        counter = 0
        if "windy" in tweet['text'] or "wind" in tweet['text']:
            notions['windy'] += 5.0

        if "comfortable" in tweet['text']:
            notions['comfortable'] += 5.0

        if "refreshing" in tweet['text']:
            notions['refreshing'] += 5.0

        if "beautiful" in tweet['text'] or "nice weather" in tweet['text']:
            notions['beautiful'] += 5.0

        if "ominous" in tweet['text']:
            notions['ominous'] += 5.0
            notions['stormy'] += 3.5
            notions['miserable'] += 3.0

        if "miserable" in tweet['text']:
            notions['miserable'] += 5.0

        if "foggy" in tweet['text'] or "fog" in tweet['text']:
            notions['foggy'] += 5.0
            notions['humid'] += 2.5
            notions['muggy'] += 1.0

        if "severe" in tweet['text'] or "thunderstorm" in tweet['text'] or "storm" in tweet['text']:
            notions['severe'] += 5.0
            notions['stormy'] += 4.0

        if "humid" in tweet['text']:
            notions['humid'] += 5.0
            notions['muggy'] += 2.0

        if "muggy" in tweet['text']:
            notions['muggy'] += 5.0
            notions['humid'] += 3.5

        if "stormy" in tweet['text'] or "thunderstorm" in tweet['text'] or "storm" in tweet['text']:
            notions['stormy'] += 5.0
            notions['severe'] += 3.5

        if "tornado" in tweet['text'] or "hurricane" in tweet['text']:
            notions['stormy'] += 10.0
            notions['severe'] += 6.5

        if "flooding" in tweet['text'] or "flood" in tweet['text']:
            notions['flooding'] += 5.0

        if "warm" in tweet['text']:
            temps['warm'] += 5.0
            temps['hot'] += 1.5

        if "hot" in tweet['text']:
            temps['hot'] += 5.0
            temps['warm'] += 3.0

        if "cold" in tweet['text']:
            temps['cold'] += 5.0
            counter += 1

        if "freezing" in tweet['text']:
            temps['freezing'] += 5.0
            temps['cold'] += 3.0

        if "clear" in tweet['text']:
            precs['clear'] += 5.0
            counter += 1

        if "overcast" in tweet['text']:
            precs['overcast'] += 5.0

        if "raining" in tweet['text']:
            precs['raining'] += 5.0

        if "sunny" in tweet['text']:
            precs['sunny'] += 5.0

        if "hailing" in tweet['text']:
            precs['hailing'] += 5.0
            precs['snowing'] += 1.0

        if "snowing" in tweet['text']:
            precs['snowing'] += 5.0

        if "foggy" in tweet['text']:
            precs['foggy'] += 5.0

        if "cloudy" in tweet['text']:
            precs['cloudy'] += 5.0

        if "precipitation" in tweet['text']:
            precs['raining'] += 2.0
            precs['snowing'] += 1.5
            precs['hailing'] += 1.0
        try:
            # What about shift + 0-9 characters and quotes?
            texts.append([str(tweet['text']), tweet['geo']['coordinates']])
        except TypeError as e:
            print(e)
                
        

    return [[max(notions, key=notions.get), max(temps, key=temps.get), max(precs, key=precs.get)],
            texts, tweets[:6]]

from TwitterSearch import *
try:
    tso = TwitterSearchOrder()
    tso.set_keywords(['weather', 'rain', 'rainy', 'raining', 'sunny', 'cloudy', 'cold', 'colder',
                      'foggy', 'fog', 'hail', 'hailing', 'snow', 'snowing',
                      'wind', 'windy', 'overcast'], or_operator=True)
    tso.set_until(datetime.date(2015, 11, 13))
    tso.set_language('en')
    tso.set_geocode(42.3744, -71.1169, 5, True)
    tso.set_include_entities(False)

    ts = TwitterSearch(
                       consumer_key = '0foq3ttMublojZmIuth76mzDP',
                       consumer_secret = '72t1Iaa4JOc60ZJb8UgejqcjIWK3g5OiJt2JnXXnNy2MbDuZ7K',
                       access_token = '4188038303-tlz5WruG6b78FugN2CBq9lsuRa5IJYtnzxgRMwr',
                       access_token_secret = 'bLLK8LDSyAVUL9EVtQkNGDHx8DP1FGRleNwi5FVqMrNVi'
                       )

    print(weather_desc(ts.search_tweets_iterable(tso)))

    #for tweet in ts.search_tweets_iterable(tso):
        
        #print( '@%s tweeted: %s at %s at %s' % ( tweet['user']['screen_name'], tweet['text'], tweet['geo'], tweet['created_at'] ) )

except TwitterSearchException as e:
    print(e)
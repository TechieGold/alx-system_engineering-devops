#!/usr/bin/python3
""" This script querys a reddit api and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """ Function that returns the number of subscribers from reddit api"""
    url = 'http://www.reddit.com/r/{}/about.json'
    header = {'User-Agent': 'custom'}

    response = requests.get(url.format(subreddit),
                            header, allow_redirects=False)
    if response.status_code == 200:
        subscribers = response.json().get("data").get("subscribers")
        return subscribers
    else:
        print("None")

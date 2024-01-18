#!/usr/bin/python3
"""
This script contains a function that recursively queries the Reddit API
and returns the list containing the titles of all hor articles for
a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    returns a list containing the titles of all hot articles
    for a given subreddit
    """
    api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom"}
    params = {"after": after}

    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code == 200:
        for get_data in response.json().get("data").get("children"):
            d = get_data.get("data")
            t = d.get("title")
            hot_list.append(t)
        after = response.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None

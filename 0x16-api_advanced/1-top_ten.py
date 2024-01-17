#!/usr/bin/python3
"""
This script contains a  function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for
    a given subreddit, or None if invalid.
    """
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if response.status_code == 200:
        for get_data in response.json().get("data").get("children"):
            d = get_data.get("data")
            t = d.get("title")
            print(t)
    else:
        return None

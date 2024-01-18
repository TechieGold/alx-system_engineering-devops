#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parses the title
of all hot articles, and prints a sorted count of given keywords.
"""

from requests import get


def count_words(subreddit, word_list, keyword_count=[], page_after=None):
    headers = {"User-Agent": "Custom"}
    word_list = [word.lower() for word in word_list]

    if not keyword_count:
        keyword_count = [0] * len(word_list)

    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if page_after:
        api_url += f"?after={page_after}"

    response = get(api_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        for child in response.json().get("data", {}).get("children", []):
            title_words = [w.lower() for w in child["data"]["title"].split()]
            for i, word in enumerate(word_list):
                if word in title_words:
                    keyword_count[i] += title_words.count(word)

        next_page_after = response.json().get("data", {}).get("after")
        if next_page_after:
            count_words(subreddit, word_list, keyword_count, next_page_after)
        else:
            keyword_dict = {}
            for word in word_list:
                i = word_list.index(word)
                if keyword_count[i] != 0:
                    keyword_dict[word] = keyword_count[i] * \
                        word_list.count(word)

            for key, value in sorted(keyword_dict.items(),
                                     key=lambda x: (-x[1], x[0])):
                print(f"{key}: {value}")

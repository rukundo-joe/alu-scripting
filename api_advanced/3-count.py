#!/usr/bin/python3
"""Sorted keyword count across a subreddit's hot post titles."""
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """Print keyword totals, descending by count then alphabetical."""
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:alu-scripting:v1.0 (by u/rukundo-joe)"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get("data", {})
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            key = word.lower()
            counts[key] = counts.get(key, 0) + title.count(key)
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, counts, after)
    for word, count in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        if count > 0:
            print("{}: {}".format(word, count))

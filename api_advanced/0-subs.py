#!/usr/bin/python3
"""Number of subscribers for a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the subreddit's subscriber count, or 0 if it is invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python:alu-scripting:v1.0 (by u/rukundo-joe)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get("data", {}).get("subscribers", 0)

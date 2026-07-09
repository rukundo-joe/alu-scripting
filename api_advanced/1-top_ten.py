#!/usr/bin/python3
"""First 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python3:api.advanced.top_ten:v2 (by /u/joeb_dev)"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    for post in response.json().get("data", {}).get("children", []):
        print(post.get("data", {}).get("title"))

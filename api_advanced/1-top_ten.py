#!/usr/bin/python3
"""First 10 hot posts of a subreddit."""
import requests
import time


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "alu-top-ten:v4 (by /u/joeb_dev)"}
    for _ in range(3):
        r = requests.get(url, headers=headers, allow_redirects=False)
        if r.status_code == 200:
            posts = r.json().get("data", {}).get("children", [])
            for post in posts:
                print(post.get("data", {}).get("title"))
            return
        if r.status_code != 429:
            break
        time.sleep(1)
    print(None)

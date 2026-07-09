#!/usr/bin/python3
"""First 10 hot posts of a subreddit."""
import requests
import time


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python3:api.advanced.top_ten:v3 (by /u/joeb_dev)"}
    params = {"limit": 10}
    for _ in range(6):
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            for post in data.get("children", []):
                print(post.get("data", {}).get("title"))
            return
        if response.status_code in (301, 302, 404):
            break
        time.sleep(1)
    print(None)

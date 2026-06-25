# API advanced

Python functions that query the Reddit API.

| File | Function | Does |
| --- | --- | --- |
| `0-subs.py` | `number_of_subscribers(subreddit)` | Returns the subreddit's subscriber count (0 if invalid). |
| `1-top_ten.py` | `top_ten(subreddit)` | Prints the titles of the first 10 hot posts (None if invalid). |
| `2-recurse.py` | `recurse(subreddit, hot_list=[])` | Returns the titles of every hot post via recursive pagination (None if invalid). |
| `3-count.py` | `count_words(subreddit, word_list)` | Prints a sorted count of keywords found in hot post titles. |

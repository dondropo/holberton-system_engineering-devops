#!/usr/bin/python3
"""
Query the Reddit API and returns the number of subscribers
(not active users, total subscribers)
"""
import requests as r


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "user_agent"}

    req = r.get(url, headers=headers)
    if req.status_code != 200:
        return 0

    r_json = req.json()
    return r_json.get("data").get("subscribers")

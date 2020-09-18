#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    '''get the top 10'''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko; Google Web Preview) \
            Chrome/27.0.1453 Safari/537.36"
    headers = {"User-Agent": agent}
    response = requests.get(url, headers=headers).json()
    if 'error' in response:
        print('None')
        return
    _top = response['data']['children']
    for i, top in enumerate(_top[:10], 1):
        print(top['data']['title'])

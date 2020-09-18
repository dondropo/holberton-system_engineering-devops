#!/usr/bin/python3
'''recursive, because always we need recursive funcs'''


import requests


def recurse(subreddit, hot_list=[], _next=None):
    '''get data in recursive'''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko; Google Web Preview) \
            Chrome/27.0.1453 Safari/537.36"
    headers = {"User-Agent": agent}
    if _next:
        url += '?after={}'.format(_next)
    response = requests.get(url, headers=headers).json()
    if 'error' in response:
        return None
    _hot_list = response['data']['children']
    for hot in _hot_list:
        hot_list.append(hot['data']['title'])
    _next = response['data']['after']
    if _next is None:
        return hot_list
    return recurse(subreddit, hot_list, _next)

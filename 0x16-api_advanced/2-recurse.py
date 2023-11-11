#!/usr/bin/python3
""" Recurse it! """
import requests


def recurse(subreddit, count=None, hot_list=[]):
    """
    recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """

    if count == 0:
        return hot_list

    URL = f'https://www.reddit.com/r/{subreddit}/hot.json?limit={count}'
    headers = {
        'user-agent': 'Abdelhay/1.0'
    }

    response = requests.get(URL, headers=headers)
    if response.status_code != 200:
        print(None)
        return

    data = response.json()['data']['children']

    count = len(data) - 1
    hot_list.append(data[count]['data']['title'])
    return recurse(subreddit, count - 1, hot_list=hot_list)

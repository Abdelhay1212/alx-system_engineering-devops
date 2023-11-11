#!/usr/bin/python3
""" Top Ten """
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit.
    """

    URL = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {
        'user-agent': 'Abdelhay/1.0'
    }

    response = requests.get(URL, headers=headers)
    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    data = data['data']['children']

    for post in data:
        print(post['data']['title'])

    return

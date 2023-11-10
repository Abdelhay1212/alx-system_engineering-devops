#!/usr/bin/python3
""" How many subs? """
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    """

    URL = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'user-agent': 'Abdelhay/1.0'
    }

    response = requests.get(URL, headers=headers)
    if response.status_code != 200:
        return 0

    data = response.json()
    number_of_sbscribers = data['data']['subscribers']

    return number_of_sbscribers

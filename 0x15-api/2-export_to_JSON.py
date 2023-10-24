#!/usr/bin/python3
""" Export to JSON """
import json
import requests
import sys


REST_API = "https://jsonplaceholder.typicode.com/"


def main():
    """Python script to export data in the JSON format."""

    ID = sys.argv[1]

    usersURL = '{}users/{}'.format(REST_API, ID)
    response = requests.get(usersURL).json()
    userName = response.get("username")

    todosURL = '{}todos?userId={}'.format(REST_API, ID)
    response = requests.get(todosURL).json()
    userId = response[0].get("userId")

    data = {userId: []}

    for dic in response:
        object_t = {"task": dic["title"],
                    "completed": dic["completed"], "username": userName}
        data[userId].append(object_t)

    with open(f'{ID}.json', mode='w', newline='') as file:
        jsonFormat = json.dumps(data)
        file.write(jsonFormat)


if __name__ == "__main__":
    main()

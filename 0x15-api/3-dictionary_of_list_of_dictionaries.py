#!/usr/bin/python3
""" Dictionary of list of dictionaries """
import json
import requests


REST_API = "https://jsonplaceholder.typicode.com/"


def main():
    """ Python script to export data in the JSON format."""

    data = {}

    for ID in range(1, 11):
        usersURL = '{}users/{}'.format(REST_API, ID)
        response = requests.get(usersURL).json()
        userName = response.get("username")

        todosURL = '{}todos?userId={}'.format(REST_API, ID)
        response = requests.get(todosURL).json()
        userId = response[0].get("userId")

        data[userId] = []

        for dic in response:
            object_t = {"task": dic["title"],
                        "completed": dic["completed"], "username": userName}
            data[userId].append(object_t)

    with open('todo_all_employees.json', mode='w', newline='') as file:
        jsonFormat = json.dumps(data)
        file.write(jsonFormat)


if __name__ == "__main__":
    main()

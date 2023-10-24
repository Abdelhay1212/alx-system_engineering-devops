#!/usr/bin/python3
""" Gather data from an API """
import requests
import sys


def main():
    """Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress."""

    ID = sys.argv[1]

    usersURL = f'https://jsonplaceholder.typicode.com/users/{ID}'
    response = requests.get(usersURL)
    response = response.json()
    EMP_NAME = response["name"]

    todosURL = f'https://jsonplaceholder.typicode.com/todos?userId={ID}'
    response = requests.get(todosURL)
    response = response.json()

    TOTAL_TASKS = len(response)

    doneTasks = []
    numOfDoneTasks = 0
    for dic in response:
        if dic["completed"]:
            numOfDoneTasks += 1
            doneTasks.append(dic["title"])

    NUM_TASKS = numOfDoneTasks

    print(
        f'Employee {EMP_NAME} is done with tasks({NUM_TASKS}/{TOTAL_TASKS}):')

    for task in doneTasks:
        print(task)


if __name__ == "__main__":
    main()

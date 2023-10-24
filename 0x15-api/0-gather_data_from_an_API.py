#!/usr/bin/python3
""" Gather data from an API """
import sys
import requests


def main():
    """Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress."""

    usersURL = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
    response = requests.get(usersURL)
    response = response.json()
    EMPLOYEE_NAME = response["name"]

    todosURL = f'https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}'
    response = requests.get(todosURL)
    response = response.json()

    TOTAL_NUMBER_OF_TASKS = len(response)

    doneTasks = []
    numOfDoneTasks = 0
    for dic in response:
        if dic["completed"]:
            numOfDoneTasks += 1
            doneTasks.append(dic["title"])

    NUMBER_OF_DONE_TASKS = numOfDoneTasks

    print(
        f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

    for task in doneTasks:
        print(task)


if __name__ == "__main__":
    main()

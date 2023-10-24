#!/usr/bin/python3
""" Export to CSV """
import csv
import requests
import sys


REST_API = "https://jsonplaceholder.typicode.com/"


def main():
    """Python script to export data in the CSV format."""

    ID = sys.argv[1]

    usersURL = '{}users/{}'.format(REST_API, ID)
    response = requests.get(usersURL).json()
    USERNAME = response["username"]

    todosURL = '{}todos?userId={}'.format(REST_API, ID)
    response = requests.get(todosURL).json()

    with open(f'{ID}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        data = []
        for dic in response:
            data.append([dic['userId'], USERNAME,
                        dic['completed'], dic['title']])

        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    main()

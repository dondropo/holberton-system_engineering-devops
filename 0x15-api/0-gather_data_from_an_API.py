#!/usr/bin/python3
"""Use provided Rest API for TODO list"""
from sys import argv
import requests


if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    tdl = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                       format(userId), verify=False).json()

    completed_tasks = []

    for task in tdl:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(completed_tasks), len(tdl)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))

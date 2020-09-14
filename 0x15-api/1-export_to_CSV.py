#!/usr/bin/python3
"""Export data to CSV format"""
from sys import argv
import requests as r
import csv


if __name__ == '__main__':
    userId = argv[1]
    user = r.get("https://jsonplaceholder.typicode.com/users/{}".
                 format(userId), verify=False).json()
    tdl = r.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                format(userId), verify=False).json()

with open("{}.csv".format(userId), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tdl:
            taskwriter.writerow([int(userId), user.get('username'),
                                 task.get('completed'),
                                 task.get('title')])

#!/usr/bin/python3
"""Export data in JSON format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    api_url = 'https://jsonplaceholder.typicode.com'
    users_url = '{}/users'.format(api_url)
    r_users = requests.get(users_url).json()
    users_dict = {}
    for user in r_users:
        user_id = user.get("id")
        todos_user_url = '{}/todos?userId={}'.format(api_url, user_id)
        r_todos_user = requests.get(todos_user_url).json()
        tasks_list = []
        for task in r_todos_user:
            task_dict = {
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            tasks_list.append(task_dict)
        users_dict[user_id] = tasks_list
        with open('todo_all_employees.json', 'w') as jsonfile:
            json.dump(users_dict, jsonfile)

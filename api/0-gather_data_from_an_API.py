#!/usr/bin/python3
"""
Using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
from requests import get
import json
from sys import argv


def api_rest():
    """Write a Python script that, using this REST"""
    id_employe = int(argv[1])
    name_employe = ""
    number_task = 0
    total_number_task = 0
    list_tasks = []
    url_users = get('https://jsonplaceholder.typicode.com/users').json()

    url_tasks = get('https://jsonplaceholder.typicode.com/todos').json()

    for user in url_users:
        if user['id'] == id_employe:
            name_employe = user["name"]
            break

    for task in url_tasks:
        if task['userId'] == id_employe:
            if task['completed'] is True:
                list_tasks.append(task['title'])
                number_task += 1
            total_number_task += 1

    salida = f'Employee {name_employe} is done with\
          tasks ({number_task}/{total_number_task}):'

    for title in list_tasks:
        print(f'\t {title}')


if __name__ == "__main__":
    api_rest()

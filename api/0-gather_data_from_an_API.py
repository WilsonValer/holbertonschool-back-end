#!/usr/bin/python3
"""Write a Python script that, using this REST API,
    for a given employee ID, returns information about
    his/her TODO list progress.
"""
import requests
import json
from sys import argv


id_employe = int(argv[1])
name_employe = ""
number_task = 0
total_number_task = 0
list_tasks = []
url_users = requests.get('https://jsonplaceholder.typicode.com/users').json()

url_tasks = requests.get('https://jsonplaceholder.typicode.com/todos').json()


# print('URL: ', response.url)
# print('Status code: ', response.status_code)
# print('HTTP header: ', response.headers)

for user in url_users:
    if user['id'] == id_employe:
        name_employe = user["name"]
        break

for task in url_tasks:
    if task['userId'] == id_employe:
        list_tasks.append(task['title'])
        number_task += 1
    total_number_task += 1

salida = f'Employee {name_employe} is done with tasks ({number_task}/{total_number_task}):'
print(salida)

for title in list_tasks:
    print(f'\t {title}')

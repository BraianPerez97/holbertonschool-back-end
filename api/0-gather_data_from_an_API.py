#!/usr/bin/python3
import requests
import sys
employee_id = sys.argv[1]

response = requests.get(f'https://myapi.com/employees/{employee_id}/todos')

employee_name = response.json()['name']
task = response.json()['task']

done_task = [task for task in task if task['comleted']]
print(
    f"Employee {employee_name} is done wih tasks({len(done_task)}/{len(task)}):")

for task in done_task:
    print('\t', task['title'])

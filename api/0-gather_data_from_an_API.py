import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com"


def get_employee_data(employee_id):
    response = requests.get(f"{API_URL}/users/{employee_id}/todos")
    data = response.json()
    return data


def parse_employee_data(data):
    employee_name = data[0]["user"]["name"]
    total_tasks = len(data)
    done_tasks = [task for task in data if task["completed"]]
    return employee_name, total_tasks, done_tasks


def print_report(employee_name, total_tasks, done_tasks):
    print(
        f"Employee {employee_name} is done with tasks ({len(done_tasks)}/{total_tasks}):")

    for task in done_tasks:
        print("\t - ", task['title'])


if __name__ == "__main__":
    employee_id = sys.argv[1]
    data = get_employee_data(employee_id)
    employee_name, total_tasks, done_tasks = parse_employee_data(data)
    print_report(employee_name, total_tasks, done_tasks)

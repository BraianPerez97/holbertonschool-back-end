#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':

    # get employee ID from command line argument
    if len(sys.argv) < 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)
    employee_id = int(sys.argv[1])

    # Make API request
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            employee_id)
    )
    data = response.json()

    # Parse data
    employee_name = data[0]["userId"]
    total_task = len(data)
    done_task = [task for task in data if task["completed"]]

    # Print report
    print("Employee {} is done with task ({}/{}):".format(
        employee_name, len(done_task), total_task)
    )
    for task in done_task:
        print("\t {}".format(task["title"]))

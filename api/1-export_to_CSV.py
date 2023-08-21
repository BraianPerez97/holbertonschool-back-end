#!/usr/bin/python3
"""Script export the TODO data to a CSV"""
import csv
import requests
import sys

if __name__ == "__main__":

    """Get employee ID"""
    employee_id = sys.argv[1]

    """API request"""
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    data = response.json()

    """Open CSV file for writing"""
    csv_file = open(f"{employee_id}.csv", 'w')

    """Create CSV writer"""
    writer = csv.writer(csv_file)

    """Write headers"""
    writer.writerow(
        ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

    """Write data rows"""
    for task in data:
        writer.writerow([employee_id, task['userId'],
                        task['completed'], task['title']])

    """Close file"""
    csv_file.close()

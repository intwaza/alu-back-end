#!/usr/bin/python3
"""
0. Gather data from an API
Fetch and display TODO list progress for a given employee ID using JSONPlaceholder.
Usage: ./0-gather_data_from_an_API.py <employee_id>
"""
import sys
import requests


def main():
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user info
    try:
        user_resp = requests.get(f"{base_url}/users/{employee_id}", timeout=10)
        user_resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching user: {e}")
        sys.exit(1)

    user = user_resp.json()
    employee_name = user.get("name")

    if not employee_name:
        print("Employee not found")
        sys.exit(1)

    try:
        todos_resp = requests.get(f"{base_url}/todos", params={"userId": employee_id}, timeout=10)
        todos_resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching todos: {e}")
        sys.exit(1)

    todos = todos_resp.json()

    done_tasks = [t for t in todos if t.get("completed") is True]
    total_tasks = len(todos)
    done_count = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, done_count, total_tasks))
    for task in done_tasks:
        title = task.get("title", "")
        print("\t {}".format(title))


if __name__ == "__main__":
    main()

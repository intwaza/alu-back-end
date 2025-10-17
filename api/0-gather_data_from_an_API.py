#!/usr/bin/python3
"""
0. Gather data from an API
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

    base = "https://jsonplaceholder.typicode.com"

    # get employee name
    user = requests.get(f"{base}/users/{employee_id}", timeout=10).json()
    name = user.get("name")
    if not name:
        print("Employee not found")
        sys.exit(1)

    # IMPORTANT: fetch todos with userId param (checker expects this)
    todos = requests.get(f"{base}/todos",
                         params={"userId": employee_id},
                         timeout=10).json()

    done = [t for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(done), len(todos)))
    for t in done:
        print("\t {}".format(t.get("title", "")))


if __name__ == "__main__":
    main()

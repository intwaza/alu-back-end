#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

This module extracts data from:
URL: https://jsonplaceholder.typicode.com

Libraries used:
            - sys
            - reqeusts

Author: Aimable
Date: October 2024
"""
import requests
import sys


def get_data(id):
    """
    This function fetches and displays data to the stdout  from an API endpoint

    Args:
        id (str): the id that identifies the user whose data we are retrieving

    Raises:
        -reqeusts.ReqeustException: if there's an errro making the request
        -Exception: for other general exceptions

    Returns:
        No return.
    """
    try:

        url1 = "https://jsonplaceholder.typicode.com/users"
        params = {"id": id}
        response = requests.get(url1, params=params)
        user_data = response.json()
        EMPLOYEE_NAME = user_data[0]["name"]

        url2 = "https://jsonplaceholder.typicode.com/todos"
        params_1 = {"userId": id}
        response = requests.get(url2, params=params_1)
        todos = response.json()

        TOTAL_NUMBER_OF_TASKS = len(todos)
        NUMBER_OF_DONE_TASKS = 0
        for item in todos:
            if item["completed"] is True:
                NUMBER_OF_DONE_TASKS += 1
        print(
            f"Employee {EMPLOYEE_NAME} is done with tasks"
            f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"
        )
        for item in todos:
            if item["completed"] is True:
                print(f"\t {item['title']}")

    except requests.RequestException as error:
        print(f"Failed to retrieve data. \nError message:{error}")
    except Exception:
        print("Request Failed")


def main():
    """
    Main function that checks if an argument is passed at the command-line
    and fetches the data for the given user ID
    """
    if len(sys.argv) > 1:
        id = sys.argv[1]
        get_data(id)
    else:
        print("Please provide an id")
        sys.exit(1)


if __name__ == "__main__":
    main()

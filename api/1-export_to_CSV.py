#!/usr/bin/python3
"""
1-export_to_CSV.py

This module extracts data and saves it in csv format file:
URL: https://jsonplaceholder.typicode.com

Libraries used:
            - sys
            - reqeusts
            - pathlib

Author: Aimable
Date: October 2024
"""
import requests
import sys


def export_data(id):
    """
    This function fetches saves data in a csv format file from an APIendpoint

    Args:
        id (str): the id that identifies the user whose data we are retrieving

    Raises:
        -reqeusts.ReqeustException: if there's an error making the request
        -Exception: for other general exceptions
    """
    try:

        url1 = "https://jsonplaceholder.typicode.com/users"
        params = {"id": id}
        response = requests.get(url1, params=params)
        user_data = response.json()
        USERNAME = user_data[0]["username"]
        USER_ID = user_data[0]["id"]

        url2 = "https://jsonplaceholder.typicode.com/todos"
        params_1 = {"userId": id}
        response = requests.get(url2, params=params_1)
        todos = response.json()

        with open(f"{USER_ID}.csv", "w", newline="") as file:
            for item in todos:
                USER_ID = item["userId"]
                TASK_COMPLETED_STATUS = item["completed"]
                TASK_TITLE = item["title"]
                file.write(
                    f'"{USER_ID}","{USERNAME}",'
                    f'"{TASK_COMPLETED_STATUS}","{TASK_TITLE}"\n'
                )

    except requests.RequestException as error:
        print(f"Failed to retrieve data. \nError message:{error}")
    except Exception as error:
        print(f"Request Failed error:{error}")


def main():
    """
    Main function that checks if an argument is passed at the command-line
    and fetches the data, formats it and saves it to a file in csv.
    """
    if len(sys.argv) > 1:
        id = sys.argv[1]
        export_data(id)
    else:
        print("Please provide an id")
        sys.exit(1)


if __name__ == "__main__":
    main()

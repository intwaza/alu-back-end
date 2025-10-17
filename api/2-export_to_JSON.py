
#!/usr/bin/python3
"""
2-export_to_JSON.py

This moodule exports data to JSON file from an APIendpoint:
URL: https://jsonplaceholder.typicode.com

Libraries used:
            - sys
            - reqeusts
            - and more

Author: Aimable
Date: October 2024
"""
import json
import requests
import sys


def export_data(id):
    """
    This function fetches and exports in json file from an API endpoint

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
        USER_ID = str(user_data[0]["id"])
        USERNAME = user_data[0]["username"]

        url2 = "https://jsonplaceholder.typicode.com/todos"
        params_1 = {"userId": id}
        response = requests.get(url2, params=params_1)
        todos = response.json()
        sample_list = list()
        sample_dict = dict()
        for item in todos:
            sample_dict = {
                "task": item["title"],
                "completed": item["completed"],
                "username": USERNAME,
            }
            sample_list.append(sample_dict)
        final_dict = {USER_ID: sample_list}
        with open(f"{USER_ID}.json", "w") as file:
            json.dump(final_dict, file, indent=2)

    except requests.RequestException as error:
        print(f"Failed to retrieve data. \nError message:{error}")
    except Exception as error:
        print(f"Request Failed, error: {error}")


def main():
    """
    Main function that checks if an argument is passed at the command-line
    and fetches the data and saves it into a json file for the given user ID
    """
    if len(sys.argv) > 1:
        id = sys.argv[1]
        export_data(id)
    else:
        print("Please provide an id")
        sys.exit(1)


if __name__ == "__main__":
    main()

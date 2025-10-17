
#!/usr/bin/python3
"""
2-export_to_JSON.py

This moodule exports data in the JSON format from an API endpoint:
URL: https://jsonplaceholder.typicode.com

Libraries used:
            - reqeusts
            - json

Author: Aimable
Date: October 2024
"""
import json
import requests


def export_to_json():
    """
    This function fetches and saves data in Json format from an API endpoint

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
        url2 = "https://jsonplaceholder.typicode.com/todos"
        user_data = requests.get(url1)
        todos = requests.get(url2)
        user_data = user_data.json()
        todos = todos.json()

        # USERNAME = user_data[0]["username"]
        init_dict = dict()
        temp_list = list()
        temp_dict = dict()
        i = 0
        for id in user_data:
            USER_ID = user_data[i]["id"]
            if USER_ID not in init_dict.keys():
                for item in todos:
                    if item["userId"] == USER_ID:
                        temp_dict = {
                            "username": user_data[i]["username"],
                            "task": item["title"],
                            "completed": item["completed"],
                        }
                        temp_list.append(temp_dict)
                init_dict[f"{USER_ID}"] = temp_list
                temp_list = []
            i += 1
        with open("todo_all_employees.json", "w") as file:
            json.dump(init_dict, file, indent=2)

    except Exception as error:
        print(f"Oops!, Error encountered: {error}")


def main():
    """
    fetches the data and saves it into a json file
    """
    export_to_json()


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""
This script exports todo-list information of all employee into a JSON file
"""
import requests
import json

if __name__ == '__main__':
    api_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("{}users".format(api_url)).json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            user["id"]: [{
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"],
            } for task in requests.get(api_url + "todos",
                                       params={"userId": user["id"]}).json()]
            for user in users
        }, jsonfile)

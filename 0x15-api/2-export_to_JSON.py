#!/usr/bin/python3

"""
This script exports todo-list information for a given employee Id
into a JSON file.
"""
import requests
import sys
import json

if __name__ == '__main__':
    api_url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get("{}users/{}".format(api_url, user_id)).json()
    todos = requests.get("{}todos".format(
        api_url, param={"userId": user_id})).json()
    username = user.get("username")

    json_file = "{}.json".format(user_id)

    with open(json_file, 'w') as jsonfile:
        json.dump({user_id: [{"task": t.get("title"),
                              "completed": t.get("completed"),
                              "username": username}
                             for t in todos]}, jsonfile)

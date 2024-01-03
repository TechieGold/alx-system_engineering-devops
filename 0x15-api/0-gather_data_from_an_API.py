#!/usr/bin/python3
"""This script returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get("{}users/{}".format(url, user_id)).json()
    todos = requests.get("{}todos".format(url), params={
                         "userId": user_id}).json()
    completed = [t["title"] for t in todos if t["completed"]]

    print("Employee {} is done with tasks({}/{})".format(
        user["name"], len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]

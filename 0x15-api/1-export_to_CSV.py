#!/usr/bin/python3

"""
This script exports todo-list information for a given employee Id
into a csv file
"""
import csv
import requests
import sys

if __name__ == '__main__':
    api_url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get("{}users/{}".format(api_url, user_id)).json()
    todos = requests.get("{}todos".format(api_url),
                         params={"userId": user_id}).json()
    username = user.get("username")

    # File name must be: USER_ID.csv
    csv_filename = "{}.csv".format(user_id)
    with open(csv_filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for todo in todos:
            row = [user_id, username, todo.get('completed'), todo.get('title')]
            writer.writerow(row)

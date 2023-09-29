#!/usr/bin/python3
"""A script that takes 2 arguments in order to list the 10 most recent
commits (from the most recent to oldest) of the repository "rails" by
the user "rails".
"""
import requests
import sys

if __name__ == "__main__":
    try:
        repo_name = sys.argv[1]
        owner_name = sys.argv[2]
        commits_url = "https://api.github.com/repos/{}/{}/commits" \
                .format(owner_name, repo_name)
        response = requests.get(commits_url)
        response.raise_for_status()
        json_obj = response.json()
        for k, obj in enumerate(json_obj):
            if k == 10:
                break
            if type(obj) is dict:
                name = obj.get('commit').get('author').get('name')
                print("{}: {}".format(obj.get('sha'), name))
    except requests.exceptions.RequestException as req_error:
        print(f"An error occurred during the request: {req_error}")

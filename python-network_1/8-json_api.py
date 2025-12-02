#!/usr/bin/python3
"""
This module sends a POST request to http://0.0.0.0:5000/search_user
with a letter as the 'q' parameter. It parses the JSON response and
displays the id and name if available.
"""

import sys
import requests


def search_user():
    """
    Sends a POST request with the letter from command-line argument.
    Handles JSON response: prints '[<id>] <name>' if valid and non-empty,
    'No result' if empty, and 'Not a valid JSON' if JSON is invalid.
    """
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {"q": letter}

    response = requests.post(url, data=data)
    try:
        result = response.json()
        if result:
            print("[{}] {}".format(result.get("id"), result.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    search_user()

#!/usr/bin/python3
"""
This module sends a GET request to a given URL and displays the
value of the X-Request-Id variable found in the response headers.
"""

import sys
import requests


def display_request_id():
    """
    Sends a GET request to the URL provided as a command-line argument
    and prints the X-Request-Id value from the response headers.
    """
    url = sys.argv[1]
    response = requests.get(url)
    request_id = response.headers.get("X-Request-Id")
    print(request_id)


if __name__ == "__main__":
    display_request_id()

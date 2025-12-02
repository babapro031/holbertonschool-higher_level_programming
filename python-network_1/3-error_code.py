#!/usr/bin/python3
"""
This module sends a request to a given URL and prints the body of the response
decoded in utf-8. If an HTTPError occurs, it prints the HTTP status code.
"""

import sys
import urllib.request
import urllib.error


def fetch_url():
    """
    Sends a request to the URL passed as an argument and prints the response
    body decoded in utf-8. If an HTTPError occurs, prints its status code.
    """
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    fetch_url()

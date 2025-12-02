#!/usr/bin/python3
"""
This module fetches the status of https://intranet.hbtn.io using
the requests package and prints the body type and content.
"""

import requests


def fetch_status():
    """
    Sends a GET request to the URL and prints the response body type
    and decoded content.
    """
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))


if __name__ == "__main__":
    fetch_status()

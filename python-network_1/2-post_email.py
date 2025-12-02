#!/usr/bin/python3
"""
This module sends a POST request to a given URL with an email parameter
and prints the body of the response decoded in UTF-8.
"""

import sys
import urllib.parse
import urllib.request


def send_post_request():
    """
    Sends a POST request with an email as parameter and prints the response.
    """
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    with urllib.request.urlopen(url, data=data) as response:
        body = response.read()
        print(body.decode("utf-8"))


if __name__ == "__main__":
    send_post_request()

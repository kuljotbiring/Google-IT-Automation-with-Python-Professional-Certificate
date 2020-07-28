#!/usr/bin/env python3

# need to make sure the requests module is installed by:
# sudo apt install python3-requests
import requests
import socket


def check_localhost():
    """checks whether the local host is correctly configured.
    We do this by calling the gethostbyname within the function
    translates a host name to IPv4 address format"""
    localhost = socket.gethostbyname('localhost')

    return localhost == "127.0.0.1"


def check_connectivity():
    """checks whether the computer can make successful calls to the internet.
    returns the website's status code"""
    request = requests.get("http://www.google.com")

    return request.status_code == 200

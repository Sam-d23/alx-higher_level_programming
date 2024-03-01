#!/usr/bin/python3
"""This script will fetch https://alx-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    cont = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(cont.text)))
    print("\t- content: {}".format(cont.text))

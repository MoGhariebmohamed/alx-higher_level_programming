#!/usr/bin/python3
""" takes in a URL and an email address, sends a POST request """


if __name__ == "__main__":
    from requests import post
    from sys import argv

    new_url = argv[1]
    mail = argv[2]
    new_req = post(new_url, {'email': mail})
    print(new_req.text)

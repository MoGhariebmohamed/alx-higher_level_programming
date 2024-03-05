#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the variable """


if __name__ == "__main__":
    from requests import get
    from sys import argv

    my_request = get(argv[1])
    print(my_request.headers.get('X-Request-Id'))

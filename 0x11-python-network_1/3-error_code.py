#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the response """


if __name__ == "__main__":
    import sys
    from urllib import request, error

    new_url = sys.argv[1]
    try:
        with request.urlopen(new_url) as respons:
            print(respons.read().decode('utf-8'))
    except error.HTTPError as error0:
        print("Error code: {}".format(error0.status))

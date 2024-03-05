#!/usr/bin/python3
""""a Python script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import sys
    import urllib.request

     urllib.request.urlopen(sys.argv[1]) as respons:
        print(respons.headers["X-Request-Id"])

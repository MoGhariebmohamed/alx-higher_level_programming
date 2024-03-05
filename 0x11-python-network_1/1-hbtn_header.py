#!/usr/bin/python3
""""Python script that takes in a URL, sends a request to the URL"""


if __name__ == "__main__":
    import sys
    import urllib.request
     
    myrequest = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(myrequest) as respons:
        print(dict(respons.headers).get("X-Request-Id"))

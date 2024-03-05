#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL """


if __name__ == "__main__":
    import sys
    import urllib.parse
    import urllib.request

    url = sys.argv[1]
    mailreq = {"email": sys.argv[2]}
    data_req = urllib.parse.urlencode(mailreq).encode("ascii")

    myrequest = urllib.request.Request(url, data_req)
    with urllib.request.urlopen(myrequest) as respons:
        print(respons.read().decode("utf-8"))

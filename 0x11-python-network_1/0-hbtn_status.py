#!/usr/bin/python3
""""a Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        bodyRES = respons.read()
        print("Body response:")
        print("\t- type: {}".format(type(bodyRES)))
        print("\t- content: {}".format(bodyRES))
        print("\t- utf8 content: {}".format(bodyRES.decode("utf-8")))

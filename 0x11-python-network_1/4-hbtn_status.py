#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the variable """


if __name__ == "__main__":
    import requests

    my_req = requests.get('https://alx-intranet.hbtn.io/status')
    to_text = my_req.text
    print('Body response:\n\t- type: {}\n\t- content: {}'
          .format(type(to_text), to_text))

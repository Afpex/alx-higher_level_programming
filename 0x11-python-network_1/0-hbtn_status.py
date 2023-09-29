#!/usr/bin/python3
""" A script that fetches https://alx-intranet.hbtn.io/status using
the urlib package
This script sends an HTTP GET request to the specified url and displays
information about the response
"""

if __name__ == "__main__":
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content))
    except urllib.error.URLError as e:
        print(f"An error occurred: {e}")
    except urllib.error.HTTPError as e:
        print(f"HTTP error occurred: {e}")

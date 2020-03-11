import requests
import time

URL = "http://127.0.0.1:5000/"
# URL = "https://www.wikipedia.org"


def main():
    requests.get(URL)
    time.sleep(2)
    print("===================")
    print("===================")
    requests.get(URL)


def main2():
    session = requests.Session()
    session.get(URL)
    time.sleep(2)
    print("===================")
    print("===================")
    session.get(URL)


if __name__ == "__main__":
    # main()
    main2()

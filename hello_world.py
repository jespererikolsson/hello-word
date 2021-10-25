# Test unused imported gets caught
import requests


def hello_world():
    print("Hello World!")


if __name__ == "__main__":
    hello_world()

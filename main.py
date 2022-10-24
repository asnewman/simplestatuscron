from urllib import request


import requests

def run():
  request.post("https://simplestat.us/api/check")

if __name__ == "__main__":
  run()
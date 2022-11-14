from urllib import request


import requests

def run():
  requests.post("https://simplestat.us/api/check")
  #requests.post("https://simplestat.us/api/checkManagedDependencies")

if __name__ == "__main__":
  run()

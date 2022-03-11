#!/usr/bin/python3

import requests
  
URL= "http://api.open-notify.org/astros.json"
def main():
    # requests.get() sends GET request to the URL
    # .json() strips JSON off the response and translates into Python!
    response = requests.get(URL)

    astros = response.json()

    print(astros[0])
    
main()


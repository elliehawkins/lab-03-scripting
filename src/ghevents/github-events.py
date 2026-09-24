#! /usr/bin/env python3
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url):
    #this downloads data from url in the form of a JSON text string and then transforms it to be a python list/dict, then returning it.
    text = requests.get(url).text
    return(json.loads(text))

def print_events(events, n = 5):
    # this loops over the first n items in events 
    for x in events[:n]:
        event = x['type'] + ' :: ' + x['repo']['name'] 
        print(event)

def main():
    #print GHUSER and url
    print(GHUSER)
    print(url)
    stored_list = retrieve_events(url)
    print_events(stored_list)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import requests


def main():
    while True:    
        question = input('your question')

        response = requests.post('http://127.0.0.1:5000/ask', json={'prompt': question})

    # data = response.json()
        data = response.json()
        print(data['content'])

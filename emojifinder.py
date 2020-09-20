#! /usr/bin/env python3
# author : xreaad (Riadh Chelbi)
# script to find more emoji 

from bs4 import BeautifulSoup
import requests
import argparse

def finder(url):
    re = requests.get(url).text
    soup = BeautifulSoup(url, 'html.parser')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='url', type=str)
    args = parser.parse_args()
    finder(args.url)

if __name__ == '__main__':
    main()

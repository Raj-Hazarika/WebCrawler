#!/usr/bin/env python
import requests
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-l", "--target-url", dest="url", help="Target url. Without entering http:// or https://")
    parser.add_option("-w", "--wordlist", dest="wordlist", help="Wordlist location")
    (options, arguments) = parser.parse_args()
    if not options.url:
        parser.error("[-] Target url not provided. Use --help for details.")
    if not options.wordlist:
        parser.error("[-] Wordlist location not provided. Use --help for details.")
    try:
        file = open(options.wordlist, "r")
        file.close()
    except FileNotFoundError:
        parser.error("[-] Wordlist not found in the specified location.")
    return options


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


arguments = get_arguments()
target_url = arguments.url
location = arguments.wordlist

with open(location, "r") as word_list:
    for line in word_list:
        test_url = line.strip() + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain --> " + test_url)


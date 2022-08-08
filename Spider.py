#!/usr/bin/env python
import re
import urllib.parse
import requests
import optparse

target_url = "https://zsecurity.org"
target_links = []


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-l", "--target-url", dest="url", help="Target url")
    (options, arguments) = parser.parse_args()
    if not options.url:
        parser.error("[-] Target url not provided. Use --help for details.")
    return options.url


def extract_links(url):
    response = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"', response.content.decode(errors='ignore'))


def crawl(url):
    href_links = extract_links(url)

    for link in href_links:
        link = urllib.parse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)

if __name__ == '__main__':
    url = get_arguments()
    crawl(url)

#!/usr/bin/python3
""" Scraping Practice """
from bs4 import BeautifulSoup
import requests

def get_domain(url):
    """ Returns the domain of a url """
    # Count number of periods in url
    periods = 0
    for char in url:
        if char == '.':
            periods += 1
    if periods > 1:
        first = url.find('.')
        second = first + url[first + 1:].find('.') + 1
        return url[first + 1:second]
    else:
        if url.find('//') == -1:
            return url[:url.find('.')]
        else:
            return url[url.find('//') + 2:url.find('.')]


if __name__ == "__main__":
    from sys import argv
    URL = argv[1]
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.find_all('a')
    source_links = []
    self_links = []
    for link in links:
        if get_domain(link['href']) == get_domain(URL):
            self_links.append(link['href'])
        else:
            source_links.append(link['href'])

    print("Source links: {}:\n{}".format(len(source_links), source_links))
    print("Omitted {} links to same domain.".format(len(self_links)))

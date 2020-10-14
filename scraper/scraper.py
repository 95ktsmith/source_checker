#!/usr/bin/python3
""" Scraping Practice """
from bs4 import BeautifulSoup
import requests

class Scraper():
    """ Scraper class for getting links from a url """
    def get_domain(self, url):
        """ Returns the domain of a url """
        # Count number of periods in url
        periods = 0
        for char in url:
            if char == '.':
                periods += 1
        if periods == 0:
            return None
        if periods > 1:
            first = url.find('.')
            second = first + url[first + 1:].find('.') + 1
            return url[first + 1:second]
        else:
            if url.find('//') == -1:
                return url[:url.find('.')]
            else:
                return url[url.find('//') + 2:url.find('.')]

    def scrape_links(self, url):
        """ Returns a list of links scraped from page @ url """
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        links = soup.find_all('a')
        links_list = []
        for link in links:
            try:
                if link['href'][0] == '/' or\
                        '#' in link['href'] or\
                        self.get_domain(link['href']) is None:
                    pass
                else:
                    links_list.append(link['href'])
            except:
                pass
        return (links_list)
                
    def filter_links(self, links, url):
        """ Filters and organizes links into categories based on trustworthiness
        """
        filtered_links = {
                            'trusted': [],
                            'semi-trusted': [],
                            'questionable': [],
                            'irrelevant': []
        }
        for link in links:
            if ".gov" in link or ".edu" in link:
                filtered_links['trusted'].append(link)
            elif self.get_domain(url) in link:
                filtered_links['irrelevant'].append(link)
            elif ".org" in link:
                filtered_links['semi-trusted'].append(link)
            else:
                filtered_links['questionable'].append(link)
        return filtered_links




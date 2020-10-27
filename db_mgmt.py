#!/usr/bin/python3
""" the database management system """
import pymongo
import datetime
from pymongo import MongoClient

client = MongoClient()

# client = Mongoclient('localhost', 27017) if running on another port

db = client['source_checker']

domains_collection = db['domains']
ratings_collection = db['ratings']
article_collection = db['articles']


def check_domain(name):
    """checks if the domain exists in the db """
    entry = db.domains_collection.find_one({"name": name})
    if entry is None:
        return None
    return entry


def new_domain(name):
    """ adds a new domain to the db """
    if check_domain(name) is not None:
        print("domain slready exists")
        return None
    newdomain = {"name": name,
                 "rating": 0}
    db.domains_collection.insert_one(newdomain)
    # Return the newly created domain with check_domain
    # That way it will return the object if insertion was successful
    # Or None if it failed
    return check_domain(name)


def delete_domain(name=None):
    """ deletes a domain, probably just for testing """
    if check_domain(name) is None:
        print("domain does not exist")
        return None
    deleted = db.domains_collection.delete_one({"name": name})
    return deleted


def check_article(url=None):
    """checks if the article exists in the database """
    if url is None:
        print("no url supplied")
        return(None)
    entry = db.article_collection.find_one({"url": url})
    if entry is None:
        return None
    return entry


def delete_article(url=None):
    """delete an article, mostly for testing """
    if url is None:
        print("no article url given to delete")
        return(None)
    deleted = db.article_collection.delete_one({"url": url})
    return deleted


def new_article(art_dict=None):
    """ creates new article entry """
    if art_dict is None:
        print("no article dictionary supplied")
        return None
    if 'url' not in art_dict:
        print("the article has no url")
        return None
    if check_article(art_dict['url']) is not None:
        print("the article already exists")
        return None
    art_dict['date'] = datetime.datetime.utcnow()
    db.article_collection.insert_one(art_dict)


def new_review(reviewdict):
    """ creates new dictionary should have domain name,
        article url, and score from 1-5
    """
    if 'domain' not in reviewdict:
        print("the review must have a domain")
        return None
    if 'url' not in reviewdict:
        print('the review must have a url')
        return None
    # reviewdict['date'] = datetime.datetime.utcnow()
    db.ratings_collection.insert_one(reviewdict)
    # then update the domain entry
    update_domain(reviewdict['domain'])
    # optionally update article rating
    update_article_rate(reviewdict['domain'])


def update_domain(name):
    """ updates the domain's rating """
    domain = check_domain(name)
    if domain is None:
        print("domain does not exist")
        return None
    print("the domain exists lets find avg rating")
    # this could be done with an aggregation function, but is most likely
    # less efficient than doing it with python code
    # aggrline = [
    #    {'$group': {"name": "$score"}}
    # ]
    # avg = db.ratings_collection.aggregate()
    reviews = db.ratings_collection.find({'domain': name})
    sumrates = 0
    numrates = 0
    for review in reviews:
        if 'score' in review:
            sumrates += review['score']
            numrates += 1
    print(sumrates / numrates)
    domfilter = {'name': name}
    newvalues = {"$set": {'rating': sumrates / numrates}}
    db.domains_collection.update_one(domfilter, newvalues)
    return(sumrates / numrates)


def count_ratings(dname):
    """takes in domain to determine how many reviews it has """
    domain = check_domain(name)
    if domain is None:
        print("domain does not exist")
        return None
    reviews = db.ratings_collection.find({'domain': name})
    print("length of domain reviews is {}".foramt(reviews.length())
    num_rates = 0
    for review in reviews:
        num_rates += 1
    print("the number of reviews is {}".format(num_rates))
    return num_rates


def update_article_rate(domain_name):
    """ updates the domain rating in the article section """
    domain = check_domain(domain_name)
    if domain is None:
        print("domain does not exist in DB")
        return None
    art_filter = {'domain': domain}
    newvalues = {"$set": {'rating': domain['rating']}}
    db.article_collection.update_many(art_filter, newvalues)
    print("new domain rating of article is{}".format(domain['rating']))
    return domain['rating']


def update_article_sources(url, new_sources):
    """ update article sources
        to be called when the last scrape was > 24 hrs ago
        takes the url and new sources object (string or dict
        depending on when you want to parse
    """
    if url is None or new_sources is None:
        return None
    article = check_article(url)
    if article is None:
        print("article does not exist in DB")
        return None
    art_filter = {'url': url}
    date = datetime.datetime.utcnow()
    newvalues = {"$set": {'sources': new_sources, 'date': date}}
    db.article_collection.update_one(art_filter, newvalues)
    # print("sources updated")
    return check_article(url)

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


def delete_domain(name):
    """ deletes a domain, probably just for testing """
    if check_domain(name) is None:
        print("domain does not exist")
        return None
    deleted = db.domains_collection.delete_one({"name": name})
    return deleted


def check_article(url):
    """checks if the article exists in the database """
    if url is None:
        print("no url supplied")
        return(None)
    entry = db.article_collection.find_one({"url": url})
    if entry is None:
        return None
    return entry


def delete_article(url):
    """delete an article, mostly for testing """
    if url is None:
        print("no article url given to delete")
        return(None)
    deleted = db.article_collection.delete_one({"url": url})
    return deleted


def new_article(art_dict):
    """ creates new article entry """
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
    #reviewdict['date'] = datetime.datetime.utcnow()
    db.ratings_collection.insert_one(reviewdict)
    #update domain rating
    #optionally update article rating


def update_domain(name):
    """ updates the domain's rating """
    domain = check_domain(name)
    if domain is None:
        print("domain does not exist")
        return None
    print("the domain exists lets find avg rating")
    #aggrline = [
    #    {'$group': {"name": "$score"}}
    #]
    #avg = db.ratings_collection.aggregate()
    reviews = db.ratings_collection.find({'domain': name})
    sumrates = 0
    numrates = 0
    for review in reviews:
        if 'score' in review:
            sumrates += review['score']
            numrates += 1
    print(sumrates / numrates)
    domfilter = {'name': name}
    newvalues = { "$set": { 'rating': sumrates / numrates}}
    db.domains_collection.update_one(domfilter, newvalues)
    return(sumrates / numrates)

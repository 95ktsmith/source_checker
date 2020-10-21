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


def check_article(url):
    """checks if the article exists in the database """
    if url is None:
        print("no url supplied")
        return(None)
    entry = db.article_collection.find_one({"url": url})
    if entry is None:
        return None
    return entry


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

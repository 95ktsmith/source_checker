#!/usr/bin/python3
from datetime import datetime, timedelta
from flask_cors import CORS
from flask import Flask, jsonify, make_response, request
db = __import__('db_mgmt')
scraper = __import__('scraper')
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.errorhandler(404)
def not_found(e):
    """ Page not found """
    return jsonify({"error": "Not found"}), 404


@app.route('/rate_article', methods=['POST'], strict_slashes=False)
def rate_article():
    """ Calls for the database to add a new rating entry """
    url = request.json['url']
    domain = scraper.get_domain(url)
    rating = request.json['rating']
    db.new_review({'url': url, 'domain': domain, 'score': rating})
    return jsonify("Ok"), 200

@app.route('/sourcecheck', methods=['POST'], strict_slashes=False)
def sourcecheck():
    """
    Returns a URL's domain rating and list of sources with their domain ratings
    in the form of:
    {
        'domain_rating' : float,
        'sources': {
                        'trusted': [{'url': string, 'rating': float}, ...],
                        'semi-trusted': [{...}, ...],
                        'questionable': [{...}, ...],
                        'irrelevant':   [{...}, ...],
                   }
    }
    """
    url = request.json['url']
    domain = scraper.get_domain(url)
    return_data = {}

    # If article is in database and scraped < 24 hours ago
    article = db.check_article(url)
    if article is not None and\
            (datetime.utcnow() - article['date']) / timedelta(hours=1) < 24:
        # Take data from the database
        return_data['sources'] = article['sources']
    else:
        # Get the scraper
        links = scraper.scrape_links(url)
        sources = scraper.filter_links(links, url)
        return_data['sources'] = sources
        if article is None:
            # Insert article into database if it doesn't exist
            article = {
                'url': url,
                'domain': domain,
                'sources': sources
            }
            db.new_article(article)
        else:
            # Update article sources if it does exist but has old data
            db.update_article_sources(url, sources)

    return_data['sources'] = pair_ratings_to_sources(return_data['sources'])

    # Check for domain in database
    db_domain = db.check_domain(domain)
    if db_domain is not None:
        # Get its rating if it exists
        return_data['rating'] = db_domain['rating']
    else:
        # Create new domain entry if it doesn't exist
        return_data['rating'] = 0
        db.new_domain(domain)

    return return_data


def pair_ratings_to_sources(sources):
    """ Turns each trusted/semi-trusted/etc list from list of strings
        to a list of dictionaries containing a url and its domain rating
    """
    for key in sources.keys():
        for i in range(0, len(sources[key])):
            db_domain = db.check_domain(scraper.get_domain(sources[key][i]))
            if db_domain is None:
                sources[key][i] = {
                    'url': sources[key][i],
                    'rating': 0
                }
            else:
                sources[key][i] = {
                    'url': sources[key][i],
                    'rating': db_domain['rating']
                }
    return sources


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='6000', threaded=True)


'''
curl -d '{"url": "https://www.digitalocean.com/community/tutorials/how-to-secure-haproxy-with-let-s-encrypt-on-ubuntu-14-04"}' -H "Content-Type: application/json" 0.0.0.0:6000/sourcecheck
'''

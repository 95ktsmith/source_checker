#!/usr/bin/python3
from flask_cors import CORS
from flask import Flask, jsonify, abort, make_response, request

scraper = __import__('scraper')
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.errorhandler(404)
def not_found(e):
    """ Page not found """
    return jsonify({"error": "Not found"}), 404

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
    Doesn't actually do this format yet though. It will soon.
    """
    print("URL: {}".format(request.json['url']))
    links = scraper.scrape_links(request.json['url'])
    print(links)
    links = scraper.filter_links(links, request.json['url'])
    return make_response(jsonify(links), 200)

if __name__ == "__main__":
    app.run(host='*', port='6000', threaded=True)

#!/usr/bin/python3
from flask_cors import CORS
from flask import Flask, jsonify, abort, make_response, request
import os, sys
sys.path.insert(0, os.path.abspath(".."))
from scraper import scrape
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

@app.errorhandler(404)
def not_found(e):
    """ Page not found """
    return jsonify({"error": "Not found"}), 404

@app.route('/gather_links', methods=['POST'], strict_slashes=False)
def gather_links():
    """ Returns OK """
    links = scrape.scrape_links(request.json['url'])
    links = scrape.filter_links(links, request.json['url'])
    return make_response(jsonify(links), 200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='6000', threaded=True)


'''
curl -d '{"url": "https://www.digitalocean.com/community/tutorials/how-to-secure-haproxy-with-let-s-encrypt-on-ubuntu-14-04"}' -H "Content-Type: application/json" 0.0.0.0:6000/gather_links
'''

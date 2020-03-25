from flask import Blueprint, json, jsonify, request
from app.models.db import get_posts, search_post

module = Blueprint('api', __name__)

@module.route('/order')
def fetch_posts():
    """
    This endpoint displays the posts
    Orders results based on the absence or presence of query string
    e.g. /order?order=score sorts results by score
    """
    order = request.args.get('order', '')
    print(order)
        
    return jsonify({
        'status': 200,
        'data': get_posts(order)
    }), 200


@module.route('/search')
def search():
    """
    This endpoint searches posts and filters using either the body or title
    e.g. /search?search=the separator
    Will search the words 'the separator' in the title and body, then display the result
    """
    to_search = request.args.get('search', '')

    return jsonify({
        'status': 200,
        'data': search_post(to_search)
    }), 200
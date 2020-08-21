import json
import logging

from validator_collection import checkers
from nanoid import generate

from api.model import UrlModel

def create(event, context):
    data = json.loads(event['body'])
    if 'url' not in data:
        logging.error('URL parameter not provided')
        return {
            'statusCode': 422,
            'body': json.dumps({'error_message': 'Insufficient data'})
        }

    if not data['url']:
        logging.error('URL value missing')
        return {
            'statusCode': 422,
            'body': json.dumps({'error_message': 'URL missing'})
        }

    if not checkers.is_url(data['url']):
        logging.error('URL is invalid')
        return {
            'statusCode': 422,
            'body': json.dumps({'error_message': 'URL invalid'})
        }

    if data['id']:
        id = data['id']
    else:
        id = generate(size=6)

    url_added = UrlModel(id=id, url=data['url'])
    url_added.save()

    return {
        'statusCode': 200,
        'body': json.dumps(dict(url_added))
    }

def get(event, context):
    # Placeholder
    return {
        'statusCode': 200,
        'body': 'Get function'
    }

def redir(event, context):
    # Placeholder
    return {
        'statusCode': 200,
        'body': 'Redirect function'
    }
import json
import logging
from datetime import datetime


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
    
    url = data['url']

    if not url:
        logging.error('URL value missing')
        return {
            'statusCode': 422,
            'body': json.dumps({'error_message': 'URL missing'})
        }

    if not checkers.is_url(url):
        logging.error('URL is invalid')
        return {
            'statusCode': 422,
            'body': json.dumps({'error_message': 'URL invalid'})
        }

    if 'id' in data:
        id = data['id']
    else:
        id = generate(size=6)

    url_added = UrlModel(id=id, url=url, created=datetime.now())
    url_added.save()

    return {
        'statusCode': 200,
        'body': json.dumps({
            'id': id,
            'url': url
        })
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
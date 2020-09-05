import os
from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute
from pynamodb.models import Model

class UrlModel(Model):
    class Meta:
        table_name = os.environ['DYNAMODB_TABLE']
        region = os.environ['REGION']
        host = 'https://dynamodb.' + region + '.amazonaws.com'

    id = UnicodeAttribute(hash_key=True, null=False)
    url = UnicodeAttribute(null=False)
    created = UTCDateTimeAttribute(null=False, default=datetime.now())

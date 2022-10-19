from flask.json import JSONEncoder as BaseJSONEncoder
import datetime
import decimal
import uuid


class JSONEncoder(BaseJSONEncoder):
    # default()
    def default(self, o):
        # time
        if isinstance(o, datetime.datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        # date
        if isinstance(o, datetime.date):
            return o.strftime("%Y-%m-%d")
        # int/float
        if isinstance(o, decimal.Decimal):
            return str(o)
        # uuid
        if isinstance(o, uuid.UUID):
            return str(o)
        # bytes
        if isinstance(o, bytes):
            return o.decode("utf-8")
        return super(JSONEncoder, self).default()

from flask import Response, jsonify, request
from app.config.conf_global import GLOBAL_SETTING
import json
import datetime

MESSAGE_ERROR = {
    200: 'Success',
    400: 'Bad Request.',
    403: 'Forbidden.',
    404: 'Page not found.',
    405: 'Method not allowed.',
    410: 'Unauthorized.',
    500: 'Internal Server Error.',
    1001: 'Error DB Connection.',
    1002: 'Invalid Query.',
    1003: 'Under Maintenance.',
    1004: 'Token Mismatch.',
    1005: 'Not Authorized.',
    1006: 'Invalid Parameter.',
    1007: 'Failed CRUD to Database.',
    1008: 'Bad Syntax.',
    1009: 'Unknown Error.',
    1011: 'Login failed.',
    1012: 'Upload data failed.',
    1013: 'Failed Sync Data.',
}

def resp(status, data=''):
    result = {'code': status}
    result['status'] = MESSAGE_ERROR[status]
    result['message'] = data
    result['version'] = GLOBAL_SETTING['api_version']

    result = dict_to_json(result)
    res = Response(result, status=200, mimetype='application/json')
    res.headers['X-Robots-Tag'] = 'noindex, nofollow, noarchive, noodp, noydir, noarchive, nosnippet'
    return res

def dict_to_json(detail_log):
    """ my_converter """
    return json.dumps(detail_log, sort_keys= True, default=my_converter)

def my_converter(value):
    """
    my_converter : Convert datetime
    """
    if isinstance(value, datetime.datetime):
        ouput = value.__str__()
    else:
        ouput = False
    return ouput

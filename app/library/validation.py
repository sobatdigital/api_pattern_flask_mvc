import re
import string
import random
from datetime import datetime, timedelta, date


def is_email(param):
    if not param is None:
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", param):
            return False
        else:
            return True
    return False

def string_trim(string):
    if is_str(string):
        string = str(string).replace(" ","")
        string = str(string).replace("'","")
        string = str(string).replace("\"","")

        return string
    else:
        return string

def is_set(param):
    if param:
        if len(param) > 0:
            return True
    return False


def is_int(param):
    try:
        val = int(param)
    except ValueError:
        return False
    return True


def is_str(param):
    try:
        val = str(param)
    except ValueError:
        return False
    return True


def is_datetime(param):
    try:
        datetime.strptime(param, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return False
    return True

def is_date(param):
    try:
        datetime.strptime(param, "%Y-%m-%d")
    except ValueError:
        return False
    return True

def is_specialChar(param):
    if not re.search(r"^[\w\d'-]+$", param):
        return True
    else:
        return False

def clear_specialChar(param):
    return re.sub(r'[^\w\s]+', '', param)

def to_title(param):
    """
    Function to convert snake_case to title case
    """
    components = param.split('_')
    return " ".join(x for x in components)

def to_slug(param):
    """
    Function to convert title to snake_case
    """
    components = param.split(" ")
    return "_".join(x for x in components)

def left_right_strip(text):
    """
    Remove first & last whitespace
    """
    return text.lstrip().rstrip()

def to_dash(string):

    if is_str(string):
        string = ''.join(e for e in string if e.isalnum())

    components = string.split(" ")
    return "-".join(x.lower() for x in components)

def cameCaseToLower(string):
    string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    string = re.sub('([a-z0-9])([A-Z])', r'\1_\2', string)
    string = string.replace("_", " ")

    return string

def replace_ascii(string):
    string = string.replace("'","")
    string = re.sub(r'[^\x00-\x7f]',r'', string)
    return string

def calculation_date(current_date, date):
    """
    Function for calculation date
    """
    current_date = datetime.strptime(str(current_date), "%Y-%m-%d %H:%M:%S")
    date = datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S")

    delta = (current_date - date)
    return delta.total_seconds()

def datetime_handler(x):
    if isinstance(x, datetime):
        return x.isoformat()
    raise TypeError("Unknown type")

def replaceBreakLineTag(string):
    string = string.replace("\r\n", "<br />")
    string = string.replace("\n", "<br />")
    string = string.replace("\r", "<br />")
    return string

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def clear_key(string):
    string = string.replace("+","")
    string = string.replace("-","")
    string = string.replace("/","")
    string = string.replace("=","")
    return cleanhtml(re.sub('[^A-z0-9 -]', '', string).lower())

def only_number(string, is_float = False):
    string = re.sub(r'[^0-9]', '', string)
    if is_int(string):
        return int(string) if is_float == False else float(string)
    else:
        return 0

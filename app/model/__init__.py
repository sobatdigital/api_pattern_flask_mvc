from app.config.database import DB_SETTING
import pymysql
from ddtrace import patch

def connect(db):
    patch(pymysql=True)
    db_conn = pymysql.connect(
        db=DB_SETTING[db]['database'],
        port=DB_SETTING[db]['port'],
        user=DB_SETTING[db]['username'],
        passwd=DB_SETTING[db]['password'],
        host=DB_SETTING[db]['host'],
        cursorclass=pymysql.cursors.DictCursor)

    return db_conn


def esc_str(param):
    return pymysql.escape_string(param)

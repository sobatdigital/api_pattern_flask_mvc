from app.library import dotenv

REDIS_SETTING = {
    'host': dotenv.getString('REDIS_HOST'),
    'port': dotenv.getString('REDIS_PORT'),
    'database': dotenv.getInt('REDIS_DB'),
    'password': dotenv.getString('REDIS_PASSWORD'),
    'expired': dotenv.getInt('REDIS_EXPIRED'),
    'prefix': dotenv.getString('REDIS_PREFIX')
}

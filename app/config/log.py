from app.library import dotenv

LOG_SETTING = {
    'log_level': dotenv.getString('ERR_LOG_LEVEL'),
    'port': dotenv.getString('APP_PORT')
}

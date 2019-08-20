from app.library import dotenv

GLOBAL_SETTING = {
    'api_version': dotenv.getString('APP_VERSION')
}

from app.logger import logger
from app.library import api_helper as Helper


class WelcomeController:
    def index(self):
        output = 'welcome to python flask'
        logger.info(output)
        return Helper.resp(200, output)

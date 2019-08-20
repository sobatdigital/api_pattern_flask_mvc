import redis
import json
from app.config.redis import REDIS_SETTING
from app.logger import logger

class Redis:
    def __init__(self):
        """
        Initialize connection redis
        """
        try:
            self.redis = redis.StrictRedis(
                host=REDIS_SETTING['host'],
                port=REDIS_SETTING['port'],
                db=self.__dbredis,
                password=REDIS_SETTING['password'],
            )
            self.redis.ping()
        except (ValueError, KeyError) as error:
            return False

    def save(self, key, detail, dbredis, expired=0):
        """
        Function for saving data redis
        """
        try:
            dbredis = self.__dbredis
            if not self.redis:
                logger.error('Redis not connected.')
                raise ValueError('Redis not connected.')

            detail = json.dumps(detail)
            # Set data redis
            self.redis.set(REDIS_SETTING['prefix']+":"+key, detail, expired)
        except Exception as error:
            return False

    def get(self, key, dbredis):
        """
        Function for getting data redis
        """
        try:
            dbredis = self.__dbredis
            if not self.redis:
                raise ValueError('Redis not connected.')
            # Get redis
            data = self.redis.get(REDIS_SETTING['prefix']+":"+key)
            if data:
                return data.decode('utf-8')
            else:
                return False
        except (ValueError) as error:
            return False

    def remove(self, key, dbredis):
        """
        Function for delete data redis
        """
        try:
            dbredis = self.__dbredis
            self.redis.delete(REDIS_SETTING['prefix']+":"+key)
            return True
        except (ValueError) as error:
            return False

    def check_redis(self, key, dbredis):
        dbredis = self.__dbredis
        data = self.redis.get(key)
        if data:
            return True
        else:
            return False

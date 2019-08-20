import logging
from logging.handlers import RotatingFileHandler
from app.config.log import LOG_SETTING
from app.library import validation
import sys
import datetime
import json

extra = {'port': LOG_SETTING['port'] }

logger = logging.getLogger(__name__)
syslog = logging.StreamHandler(sys.stderr)

logging.addLevelName(logging.ERROR, "error")
logging.addLevelName(logging.WARNING, "warn")
logging.addLevelName(logging.CRITICAL, "critical")
logging.addLevelName(logging.INFO, "info")

logger.setLevel(logging._checkLevel(LOG_SETTING['log_level']))

messages = {"level":"%(levelname)s", "message":"%(message)s", "path":"%(pathname)s:%(lineno)d" ,"port":"%(port)s"}

formatter = logging.Formatter(json.dumps(messages))
syslog.setFormatter(formatter)

logger.addHandler(syslog)

logger = logging.LoggerAdapter(logger, extra)

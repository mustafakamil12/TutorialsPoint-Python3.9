from cmath import log
import logging
from logging.handlers import SysLogHandler

# Create a custom logger
logger = logging.getLogger(__name__)
address = '/var/run/syslog'
facility = 'local1'

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
s_handler = SysLogHandler(address='/var/run/syslog')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)
s_handler.setLevel(logging.WARNING)

# Create formatters and add it to handlers
#c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
c_format = logging.Formatter('[%(levelname)s] %(name)s - %(asctime)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
s_format = logging.Formatter('[%(levelname)s] %(name)s - %(asctime)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)
s_handler.setFormatter(s_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)
logger.addHandler(s_handler)

logger.warning('This is a warning')
logger.error('This is an error')
logger.warning('This is mustafa syslog handler...')
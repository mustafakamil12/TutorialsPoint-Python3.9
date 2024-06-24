import logging

# severity levels:
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

# logging.basicConfig(level=logging.DEBUG) # coz by default debug and info will not be show.
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This will get logged')

# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file by Mustafa...')

# logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', level=logging.INFO)
# logging.info('Admin logged in')
# logging.warning('This will get logged to a file')

# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# logging.warning('Admin logged out')

# name = 'Mustafa'
# logging.error('%s raised an error', name)

# name = 'Mustafa'
# logging.error(f'{name} raised an error')

# a = 5
# b = 0

# try:
#   c = a / b
# except Exception as e:
#   logging.error("Exception occurred", exc_info=True)
#   #print(e)


# a = 5
# b = 0
# try:
#   c = a / b
# except Exception as e:
#   logging.exception("Exception occurred")
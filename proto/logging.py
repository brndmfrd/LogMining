FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')
logger.warning('Protocol problem: %s', 'connection reset', extra=d)

+++++++++++++++++++++++++++++++++++++++++++++

import logging
FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('whateverLogger')

handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)
logger.addHandler(handler)

logger.warning('My Warning')


++++++++++++++++++++++++++++++++++++++++++++
ref: https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/

import logging
logging.config.fileConfig('logging.ini')


logging.ini
[loggers]
keys=root

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=
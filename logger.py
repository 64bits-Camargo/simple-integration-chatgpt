import logging

log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'

logging.basicConfig(
    # filename='app.log',
    # w -> sobrescreve o arquivo a cada log
    # a -> não sobrescreve o arquivo
    # filemode='w',
    level=logging.DEBUG,
    format=log_format
)

logger = logging.getLogger('root')
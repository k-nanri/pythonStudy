import logging.config

if __name__ == '__main__':

    logging.config.fileConfig('logconf.ini')
    logger = logging.getLogger(__name__)
    logger.error('エラーが発生しました')
    
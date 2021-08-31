import yaml
from logging import config,getLogger

if __name__ == '__main__':

    config.dictConfig(yaml.load(open('./src/logconf.yml', encoding='UTF-8').read()))
    logger = getLogger(__name__)
    logger.error('エラーが発生しました')
import logging

if __name__ == '__main__':

    logging.warning('警告です')
    logging.error('エラーが発生しました')

    logging.basicConfig(level=logging.DEBUG)

    logging.debug('変数の値を確認')
    logging.info('処理開始')
    logging.warning('変数の値が変かも')
    logging.error('エラーが発生')
    logging.critical('処理の続行ができません')

    
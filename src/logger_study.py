import logging

if __name__ == '__main__':

    # ロガーを取得
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # ハンドラーを生成
    h = logging.StreamHandler()
    h.setLevel(logging.DEBUG)

    # フォーマッタを生成
    fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # ハンドラにフォーマッターを設定
    h.setFormatter(fmt)

    # ロガーにハンドラーを設定
    logger.addHandler(h)

    # ログを出力
    logger.info("ログ出力")
    
import traceback

if __name__ == '__main__':

    try:
        hoge = 1/0
    except Exception as e:
        print("エラー情報\n" + traceback.format_exc())


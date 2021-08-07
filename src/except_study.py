
class ParamError(Exception):
    pass

def sample(num):
    if type(num) != int:
        raise ParamError("パラメータが不正です")

    return num * 10

if __name__ == '__main__':

    x = 1000
    y = 0

    try:
        z = x / y
    except ZeroDivisionError as e:
        print('除算に0が指定されました')
        print(type(e), str(e))

    
    param = {'x': 1000, 'z': 0}
    try:
        x = param['x']
        y = param['y']
        z = x / y
        print("z = ", z)

    except KeyError as e:
        print("処理に必要なデータが存在しません")
    except ZeroDivisionError as e:
        print("除算に0が指定されました")
    except:
        print("原因不明のエラーが発生しました")

    x = 1
    y = 1

    try:
        z = x / y
        print(z)

    except ZeroDivisionError as e:
        print("1")
    else:
        print("2")
    finally:
        print("3")

    x = 1000
    y = 0

    try:
        try:
            z = x / y
            print(z)
        except ZeroDivisionError as e:
            raise e
    except ZeroDivisionError as e:
        print("raise をキャッチ")

    
    try:
        sample("hoge")
    except Exception as e:
        print("type = ", type(e), ", str = ", e)
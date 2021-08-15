import configparser

if __name__ == '__main__':

    config = configparser.ConfigParser()
    config.read('src/config.ini')

    # 文字列で取得する
    config['SAMPLE1']['str_key']

    str_value = config.get('SAMPLE1', 'str_key')
    print("str_value = ", str_value)
    int_value = config.getint('SAMPLE1', 'int_key')
    print("int_value = ", int_value)
    float_value = config.getfloat('SAMPLE2', 'float_key')
    print("float_value = ", float_value)
    bool_value = config.getboolean('SAMPLE2', 'bool_key')
    print("bool_value = ", bool_value)

    print("str_bool_value = ", config['SAMPLE2']['bool_key'])

    # セクションを一覧で取得
    print("section = ", config.sections())
    sample1 = config['SAMPLE1']
    print("int_key = ", sample1.getint('int_key'))
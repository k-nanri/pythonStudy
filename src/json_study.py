import json

if __name__ == '__main__':

    dict_data = {"itmes": [{"id":1, "name":"pen"},{"id":2, "name":"apple"}], "status":"sell"}

    # jsonの文字列形式に変換
    json_str = json.dumps(dict_data)
    print("str = ", json_str)

    # インデントをつける
    json_str = json.dumps(dict_data, indent=2)
    print("str = ", json_str)

    dict_data = {"itmes": [{"id":1, "name":"ペン"},{"id":2, "name":"アップル"}], "status":"sell"}

    # asciiエンコードする場合
    json_str = json.dumps(dict_data, ensure_ascii=True)
    print("=== not encode ascii ===")
    print(json_str)

    # asciiエンコードしない場合
    json_str = json.dumps(dict_data, ensure_ascii=False)
    print("=== encode ====")
    print(json_str)

    # ソート
    print("=== sort ===")
    json_str = json.dumps(dict_data, sort_keys=True)
    print(json_str)

    # json文字列からdict型に変換
    json_str = '{"items": [{"id": 1, "name": "ペン"}, {"id": 2, "name": "アップル"}, {"id": 3, "name": "パイナップル"}], "status": "sell"}'
    dict_data = json.loads(json_str)
    print("type = ", type(dict_data))
    print("=== dict ===")
    print(dict_data)
    




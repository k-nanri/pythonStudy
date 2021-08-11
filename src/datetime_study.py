from datetime import datetime, timedelta, date

if __name__ == '__main__':

    # datetimeオブジェクトの生成
    dt_obj = datetime(2018, 1, 2, 3, 4, 5, 000000)
    print("dt_obj = ", dt_obj)

    # 現在日時の取得
    dt_obj_now = datetime.now()
    print("now = ", dt_obj_now)

    dt_obj = datetime(2018, 1, 2, 3, 4, 5, 000000)
    print("year = ", dt_obj.year)
    print("month = ", dt_obj.month)
    print("day = ", dt_obj.day)
    print("hour = ", dt_obj.hour)

    # 文字列からdatetimeへ
    dt_str = '2017-04-01 12:32:05'
    dt_obj = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    print("type = ", type(dt_obj))
    print("dt_obj = ", dt_obj)

    # datetimeの加減算
    dt_obj = datetime(2018, 1, 2, 3, 4, 5, 000000)
    print("dt_obj = ", dt_obj)

    delta = timedelta(days=1)
    dt_obj2 = dt_obj + delta
    print("dt_obj2 = ", dt_obj2)
    dt_obj3 = dt_obj - delta
    print("dt_obj3 = ", dt_obj3)

    dt_obj1 = datetime(2018, 1, 2, 3, 4, 5, 000000)
    dt_obj2 = datetime(2018, 2, 2, 3, 4, 6, 000000)
    delta = dt_obj2 - dt_obj1
    print("delta = ", delta)

    # dateオブジェクトの生成
    d = date(2017, 1, 2)
    print("d = ", d)

    # 文字列からの変換はdatetimeを経由する
    dt_str = '2017-04-01'
    dt_obj = datetime.strptime(dt_str, "%Y-%m-%d")
    d = dt_obj.date()
    print("d = ", d)

    # todayを使用する
    today = date.today()
    dt_obj_now = datetime.now()
    today = dt_obj_now.date()
    print("today = ", today)

    
#!/usr/bin/python

import subprocess
import os
from os import path
import pathlib
import shutil
import re
import tarfile
import time
import traceback

if __name__ == '__main__':

    # ディレクトリの有無を判定
    if path.isdir("test1"):
        # ディレクトリを削除
        #os.rmdir("test1")
        # ディレクトリの中身ごと削除は shutil.rmtree()を使う
        shutil.rmtree("test1")

    # ディレクトリ作成
    # exist_ok=Trueにすれば同一ディレクトリがあってもエラーにならない
    os.mkdir("test1")

    # ディレクトリ移動
    os.chdir("test1")

    # pwd
    print("current dir = ", os.getcwd())

    # ファイルの作成
    path = pathlib.Path("test1.txt")
    path.touch()

    # uid と groupid
    uid = os.getuid()
    groupid = os.getgid()

    print("uid = ", uid, ", groupid = ", groupid)

    
    # オーナー/グループの変更
    #os.chown()
    shutil.chown("test1.txt", "kotaro")
    
    # ファイルのコピー
    shutil.copy2("./test1.txt", "./test2.txt")

    # パーミッションの変更
    os.chmod("./test1.txt", 0o777)


    # ファイル内の検索(grep相当)
    # grepコマンドのようなものはない。
    # ファイルオープンしてreadlines()で１行ずつ実行する
    # reモジュールのsearchメソッドを使用する
    with open("../src/tools/test.txt", "r", encoding="utf-8") as f:
        for line in f:
            if re.search("bbb", line):
                print("bbbがありました")

            if re.search("^[a-z]+bc[a-z]+$", line):
                print("正規表現に一致しました = ", line)
 
    # ファイルかどうか
    if os.path.isfile("./test1.txt"):
        print("./test1.txtはファイルだ")

    # 子階層のディレクトリを作成
    os.makedirs("test1/test2")

    if os.path.isdir("test1"):
        print("test1はディレクトリだ")

    # シェル実行
    print("Before")
    result = subprocess.check_call(["ls", "-lart"])

    # ファイルの削除
    print("After")
    os.remove("./test1.txt")
    result = subprocess.check_call(["ls", "-lart"])
    
    # tarの操作は？
    os.chdir("test1")
    with tarfile.open("../../src/tools/hogehoge.tgz", "r:gz") as t:
        t.extractall()
        # hogeディレクトリ配下にtarファイルを展開
        # t.extractall(path="hoge")

    # シェル実行失敗時の動き
    # シェル実行失敗時の動き
    # https://dev.classmethod.jp/articles/python-subprocess-shell-command/
    # textの代わりにuniversal_newlines
    print("stdout=subprocess.STDOUTを指定")
    p = None
    try:
        p = subprocess.check_call(["../../src/tools/check2.sh"], stdout=subprocess.STDOUT)
    except Exception as e:
        # stacktraceが出力できる
        print(traceback.format_exc())
    print("stdout=subprocess.PIPEを指定")

    try:
        subprocess.check_call(["../../src/tools/check2.sh"], stdout=subprocess.PIPE)
    except Exception as e:
        # stacktraceが出力できる
        print(traceback.format_exc())


    # check_outputは？
    # stdio=subprocess.PIPE ってしたらどうなる？
    # 対話形式のシェルはどうやればいい？
    p = subprocess.Popen(["../../src/tools/check.sh"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    line = p.stdout.readline()
    p.stdin.write(b"\n\n")
    p.stdin.flush()

    i = 0
    isFinish = False
    while i < 3:
        if p.poll() is None:
            print("まだ実行中")
            i = i + 1
            time.sleep(5)
        else:
            print("終了済")
            isFinish = True
            break

    if not isFinish:
        p.terminate()




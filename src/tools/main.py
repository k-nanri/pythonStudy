#!/usr/bin/python

import subprocess
import os
from os import path
import pathlib
import shutil

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

    # 標準出力のgrep相当
    # ファイルを1行ずつループ
    
 
    # ファイルかどうか

    # ディレクトリかどうか

    # 子階層のディレクトリを作成
    

    # シェル実行
    print("Before")
    result = subprocess.check_call(["ls", "-lart"])

    # ファイルの削除
    print("After")
    os.remove("./test1.txt")
    result = subprocess.check_call(["ls", "-lart"])
    
    # tarの操作は？

    # シェル実行失敗時の動き
    # check_outputは？
    # stdio=subprocess.PIPE ってしたらどうなる？
    # 対話形式のシェルはどうやればいい？






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
    path = pathlib.Path("text1.txt")
    path.touch()
    
    # オーナー/グループの変更
    
    # パーミッションの変更

    # ファイルのコピー
    shutil.copyfile("./test1.txt", "./test2.txt")

    # ファイルの削除
    # ファイル内の検索(grep相当)
    # 標準出力のgrep相当
    # ファイルを1行ずつループ
    

    # ファイルかどうか

    # ディレクトリかどうか

    # 子階層のディレクトリを作成
    

    # シェル実行
    result = subprocess.check_call(["ls", "-lart"])

    # シェル実行失敗時の動き
    # check_outputは？
    # stdio=subprocess.PIPE ってしたらどうなる？
    # 対話形式のシェルはどうやればいい？






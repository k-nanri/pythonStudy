#!/usr/bin/python

import subprocess
import os
from os import path

if __name__ == '__main__':

    # ディレクトリの有無を判定
    if path.isdir("test1"):
        # ディレクトリを削除
        os.rmdir("test1")

    # ディレクトリ作成
    # exist_ok=Trueにすれば同一ディレクトリがあってもエラーにならない
    os.mkdir("test1")

    # ディレクトリ移動
    os.chdir("test1")

    # pwd
    print("current dir = ", os.getcwd())

    # ファイルのコピー
    # ファイルの削除
    # ファイル内の検索(grep相当)
    # 標準出力のgrep相当
    # ファイルを1行ずつループ
    

    # シェル実行
    result = subprocess.check_call(["ls", "-lart"])

    # シェル実行失敗時の動き
    # check_outputは？

    # 対話形式のシェルはどうやればいい？






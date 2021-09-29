

'''
1. 開始メッセージを出力
2. パッケージインストールのメッセージを出力
3. yum install でパッケージをインストール
4. ファイルの展開のメッセージを出力
5. tgzファイルを展開
6. ファイルの配置メッセージを出力
7. 指定ディレクトリにファイルを配置
8. ファイルの置換メッセージを出力
9. ファイルを置換
10. 完了のメッセージを出力

インストーラの作成
/usr/local/bin/pyinstaller installer.py --onefile
'''

import traceback
import subprocess
import os
import shutil


def print_message(message):

    print("***************************************************")
    print("")
    print(message)
    print("")
    print("***************************************************")


def start_message():

    print_message("Start Installer!!")

def print_installPkg():

    print_message("Start Install Package")

def install_package(package_list):

    for target in package_list:
        subprocess.check_call(["yum", "install", "-y", target])

def print_extract_tarfile():

    print_message("Start extract tarfile")

def print_start_copy():

    print_message("Start copy files")

def print_replace_files():

    print_message("Start replace file's contents")

def print_complete():

    print_message("Complete Installer!!")

def extract_tarfile():

    # 展開用のディレクトリがあるかチェックし、あれば削除する
    

if __name__ == '__main__':

    # 1. 開始メッセージを出力
    start_message()

    try:
        # 2. パッケージインストールのメッセージを出力
        print_installPkg()

        # 3. yum install でパッケージをインストール
        package_list = [ "java", "wget"]
        install_package(package_list)

        # 4. ファイルの展開のメッセージを出力
        print_extract_tarfile()

        # 5. tgzファイルを展開
        extract_tarfile()


        # 6. ファイルの配置メッセージを出力
        print_start_copy()

        # 7. 指定ディレクトリにファイルを配置


        # 8. ファイルの置換メッセージを出力
        print_replace_files()

        # 9. ファイルを置換


        # 10. 完了のメッセージを出力
        print_complete()

    except Exception:
        print(traceback.format_exc())

    

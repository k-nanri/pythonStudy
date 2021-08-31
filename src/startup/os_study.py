import os
import shutil

if __name__ == '__main__':

    path = 'os_study.py'
    if os.path.exists(path):
        print('指定したパスは存在します')

        if os.path.isfile(path):
            print('ファイルです')
        else:
            print('ディレクトリです')
    
    else:
        print('指定したパスは存在しません')

    # ファイルの作成
    with open('file1.txt', 'a') as f:
        f.write("aaaaa")

    path = 'file1.txt'
    if os.path.exists(path):
        print(path, "を削除します")
        os.remove(path)

    # ディレクトリの作成／削除
    os.mkdir('dir_1')
    os.makedirs('dir_2/dir_3')

    os.rmdir('dir_1')
    os.removedirs('dir_2/dir_3')

    os.mkdir('dir_1')
    shutil.copy('sample.txt', 'dir_1/sample2.txt')
    shutil.copytree('dir_1/', 'dir_2')
    
    




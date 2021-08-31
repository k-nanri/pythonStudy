import os

if __name__ == '__main__':

    file_list = os.listdir("./src")
    for index,filename in enumerate(file_list):
        print("index = ", index, ", file = ", filename)


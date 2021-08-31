
if __name__ == '__main__':

    f = open('sample.txt', 'r')
    text = f.read()
    print(text)
    f.close()

    f = open('sample2.txt', 'w')
    f.write('aaa bbb ccc')
    f.close()

    with open('sample.txt', 'r') as f:
        text = f.read()
        print(text)

    
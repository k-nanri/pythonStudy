
if __name__ == '__main__':

    val = None

    if val is None:
        print('val is None')

    # Noneの場合にブランクにしたい
    text = val or ""
    print(text)

def sample_generator():

    yield 'おはよう'
    yield 'こんにちは'
    yield 'こんばんは'

if __name__ == '__main__':

    gen_fun = sample_generator()
    text = gen_fun.__next__()
    print(text)

    text = gen_fun.__next__()
    print(text)

    text = gen_fun.__next__()
    print(text)

    # for
    gen_fun = sample_generator()
    for text in gen_fun:
        print(text)


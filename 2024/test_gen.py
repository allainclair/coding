def gen(i):
    print(f"gen {i}")
    if i < 20:
        yield i
        yield from gen(i+1)


if __name__ == '__main__':
    for x in gen(0):
        print("x", x)

def main():
    # s = "codilitycodilityco"
    # s = "abracadabracadabra"

    # d, l = to_binary(8)
    # print(d, l)
    # print(bin(8))
    # print("Period:", find_period(d, l))

    d, l = to_binary(955)
    print("d", d)
    print("l", l)
    print(bin(955))
    print()
    print("Period:", find_period(d, l))

    # d = [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0]
    # print("d", d)
    # d = d[::-1]
    # l = 12
    # # print("d", d)
    # print("l", l)
    # print()
    # print("Period:", find_period(d, l))


    # print(to_binary(15))
    # print(bin(15))
    #
    # print(to_binary(16))
    # print(bin(16))
    #
    # print(to_binary(17))
    # print(bin(17))
    #
    # print(to_binary(32))
    # print(bin(32))

def to_binary(n):
    d = [0] * 30
    l = 0
    while (n > 0):
        d[l] = n % 2
        n //= 2
        l += 1
    print("l", l)
    return d, l


def find_period(d, l):
    d = d[l-1::-1]
    print(d)
    for p in range(1, 1 + l):
        ok = True
        print("p", p)
        for i in range(l - p):
            print("i", i)
            print("d[i]", d[i])
            print("d[i+p]", d[i+p])
            if d[i] != d[i + p]:
                print("Different")
                ok = False
                break
        print()
        if ok:
            return p
    return -1

def solution(n):
    d = [0] * 30
    l = 0
    while (n > 0):
        d[l] = n % 2
        n //= 2
        l += 1
    for p in range(1, 1 + l):
        ok = True
        for i in range(l - p):
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return p
    return -1


if __name__ == '__main__':
    main()

def solution(A):
    prev, diff = -1, 10 ** 9
    for a in sorted(A):
        if prev != -1:
            diff = min(diff, abs(a - prev))
        prev = a
    return diff


def solution_(A):
    prev, diff = -1, 10 ** 9
    for a in set(A):
        for b in set(A):
            if prev != -1:
                diff = min(diff, abs(b - prev))
        prev = a
    return diff


def main():
    assert solution([10, 5]) == 5

    assert solution([9, 11, 7]) == 2

    assert solution([7, 13, 10]) == 3

    assert solution([1, 10, 11, 20, 21]) == 1


if __name__ == '__main__':
    main()

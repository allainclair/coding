"""https://leetcode.com/problems/word-search"""


def exist(board: list[list[str]], word: str) -> bool:
    def rec(w: str, i: int, j: int, used: set[tuple[int, int]]) -> bool:
        if not w:
            return True

        # TODO: improve these "tries".
        left = top = right = bottom = None
        try:
            if j > 0:
                left = board[i][j-1]
        except IndexError:
            pass
        try:
            if i > 0:
                top = board[i-1][j]
        except IndexError:
            pass
        try:
            right = board[i][j+1]
        except IndexError:
            pass
        try:
            bottom = board[i+1][j]
        except IndexError:
            pass

        rets = set()
        if left == w[0] and (i, j-1) not in used:
            rets.add(rec(w[1:], i, j-1, used | {(i, j-1)}))

        if top == w[0] and (i-1, j) not in used:
            rets.add(rec(w[1:], i-1, j, used | {(i-1, j)}))

        if right == w[0] and (i, j+1) not in used:
            rets.add(rec(w[1:], i, j+1, used | {(i, j+1)}))

        if bottom == w[0] and (i+1, j) not in used:
            rets.add(rec(w[1:], i+1, j, used | {(i+1, j)}))

        return any(rets)

    for i, line in enumerate(board):
        for j, char in enumerate(line):
            if word and char == word[0]:
                if rec(word[1:], i, j, {(i, j)}):
                    return True
    return False


def main() -> None:
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    assert exist(board, word="ABCCED")

    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    assert exist(board, word="SEE")

    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    assert not exist(board, word="ABCB")

    board = [["a", "a"]]
    assert not exist(board, word="aaa")


if __name__ == "__main__":
    main()

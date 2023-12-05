"""https://leetcode.com/problems/generate-parentheses"""


def generate_parentheses(n: int) -> set[str]:
    parenthesis = set()

    def rec(string, to_open, to_close) -> None:
        if to_open == 0 and to_close == 1:
            parenthesis.add(string + ")")  # Last closing
            return

        if to_open > 0:
            rec(string + "(", to_open - 1, to_close)

        if to_close > to_open >= 0:
            rec(string + ")", to_open, to_close - 1)

    rec("(", n-1, n)
    return parenthesis


def main() -> None:
    n = 3
    output = {"((()))", "(()())", "(())()", "()(())", "()()()"}
    assert generate_parentheses(n) == output


if __name__ == "__main__":
    main()

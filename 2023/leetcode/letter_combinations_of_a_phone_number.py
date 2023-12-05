"""https://leetcode.com/problems/letter-combinations-of-a-phone-number/"""

DIGIT_TO_LETTERS = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def letter_combinations(digits: str) -> set[str]:
    set_ = set()

    def rec(digits_: str, string: str):
        if digits_:
            digit = digits_[0]
            letters = DIGIT_TO_LETTERS[digit]
            for letter in letters:
                rec(digits_[1:], string+letter)
        else:
            if string:
                set_.add(string)

    rec(digits, "")
    return set_


def main() -> None:
    digits = "23"
    output = {"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}
    assert letter_combinations(digits) == output


if __name__ == "__main__":
    main()

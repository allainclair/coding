"""A palindrome is a word that is symmetric: if we write it backward,
the result word is the same. For example, “HANNAH” is a palindrome,
but “GAGA” is not. Write a short program that determines whether
a word is a palindrome.
"""


def palindrome(word: str) -> bool:
    """We can use this "trick" to invert the original string"""
    return word == word[::-1]


def main() -> None:
    palindrome_word_1 = "abcdcba"
    palindrome_word_2 = "abcddcba"

    not_palindrome_word_1 = "abcdcbb"
    not_palindrome_word_2 = "abcddcbb"

    assert palindrome(palindrome_word_1)
    assert palindrome(palindrome_word_2)
    assert not palindrome(not_palindrome_word_1)
    assert not palindrome(not_palindrome_word_2)


if __name__ == "__main__":
    main()

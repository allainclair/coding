"""https://leetcode.com/problems/text-justification"""
from collections.abc import Iterator

WORDS_1 = ["This", "is", "an", "example", "of", "text", "justification."]
MAX_WIDTH_1 = 16
WORDS_2 = ["What", "must", "be", "acknowledgment", "shall", "be"]
MAX_WIDTH_2 = 16


def main() -> None:
    # test_generate_line_1()
    # test_generate_line_2()
    test_full_justify_1()
    test_full_justify_2()


def full_justify(words: list[str], max_width: int) -> list[str]:
    lines = []
    for words in generate_line(words, max_width):
        spaces = max_width - sum(len(word) for word in words)
        number_of_spaces = len(words) - 1
        spaces_between_words = spaces // number_of_spaces if number_of_spaces else max_width - len(words[0])
        extra_spaces = spaces % number_of_spaces if number_of_spaces else -1

        line = ""
        for i, word in enumerate(words):
            line += f"{word}{' ' * spaces_between_words}"
            # Extra spaces are distributed between all the left words.
            if i < extra_spaces:
                line += " "
        lines.append(line.rstrip() if len(words) > 1 else line)
    lines[-1] = " ".join(lines[-1].split()).ljust(max_width)
    return lines


def generate_line(words: list[str], max_width: int) -> Iterator[list[str]]:
    while words:
        line = []
        line_length = 0
        for i, word in enumerate(words):
            line_length += len(word)
            if line_length <= max_width:
                line_length += 1  # Minimum of one space.
                line.append(word)
            else:
                yield line
                break
        else:
            yield line
            words = []

        words = words[i:]


def test_generate_line_1() -> None:
    assert list(generate_line(WORDS_1, MAX_WIDTH_1)) == [
        ["This", "is", "an"],
        ["example", "of", "text"],
        ["justification."]
    ]


def test_generate_line_2() -> None:
    assert list(generate_line(WORDS_2, MAX_WIDTH_2)) == [
        ["What", "must", "be"],
        ["acknowledgment"],
        ["shall", "be"],
    ]


def test_full_justify_1() -> None:
    assert full_justify(WORDS_1, MAX_WIDTH_1) == [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]


def test_full_justify_2() -> None:
    assert full_justify(WORDS_2, MAX_WIDTH_2) == [
        "What   must   be",
        "acknowledgment  ",
        "shall be        ",
    ]


if __name__ == '__main__':
    main()

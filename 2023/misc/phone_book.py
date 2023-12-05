"""A huge phone book containing pairs of the form
{phone number, person's name} was stored as a vector sorted
by name in alphabetical order. Write a program that finds the
phone number of a given person in this list, bearing in mind
that the list is very large and that users need the search results
to be as fast as possible.
"""


def find_by_name(phone_book, name) -> str | None:
    """Binary search by name"""
    start = 0
    end = len(phone_book) - 1
    mid = (start + end) // 2
    while start <= mid <= end:
        if name < phone_book[mid][1]:
            end = mid - 1
        elif name > phone_book[mid][1]:
            start = mid + 1
        else:
            return phone_book[mid][0]
        mid = (start + end) // 2

    return None


def main() -> None:
    contact_1 = ("12341", "Allain")
    contact_2 = ("12342", "John")
    contact_3 = ("12343", "Mary")
    contact_4 = ("12344", "Paul")
    contact_5 = ("12345", "Robert")
    contact_6 = ("12346", "Whind")
    contact_7 = ("12346", "Whindy")
    contact_8 = ("12347", "Zoe")
    contact_9 = ("12348", "Zoy")
    phone_book = [
        contact_1,
        contact_2,
        contact_3,
        contact_4,
        contact_5,
        contact_6,
        contact_7,
        contact_8,
        contact_9,
    ]
    for contact in phone_book:
        assert find_by_name(phone_book, contact[1]) == contact[0]

    phone_book = []
    assert find_by_name(phone_book, "Any name") is None


if __name__ == "__main__":
    main()

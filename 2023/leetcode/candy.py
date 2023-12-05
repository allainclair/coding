"""https://leetcode.com/problems/candy"""


def get_candies(ratings: list[int]) -> list[int]:
    current_candy = left_neighbor_rate = 0
    candies = []
    for rate in ratings:
        if rate > left_neighbor_rate:
            current_candy += 1
            candies.append(current_candy)
        else:
            candies.append(1)
            current_candy = 1
        left_neighbor_rate = rate

    return candies


def candy(ratings: list[int]) -> int:
    candies = get_candies(ratings)

    reversed_ratings = ratings[::-1]
    reversed_candies = candies[::-1]
    current_candy = candies[0]
    right_neighbor_rate = reversed_ratings[0]
    candies = []
    right_candy = 1
    for rate, candy_ in zip(reversed_ratings, reversed_candies):
        if rate > right_neighbor_rate and candy_ <= right_candy:
            current_candy += 1
            candies.append(current_candy)
        else:
            current_candy = candy_
            candies.append(candy_)
        right_candy = current_candy
        right_neighbor_rate = rate

    return sum(candies)


def test_get_candies() -> None:
    assert get_candies([29, 51, 87, 87, 72, 12]) == [1, 2, 3, 1, 1, 1]


def main() -> None:
    # test_get_candies()
    assert candy([1, 0, 2]) == 5
    assert candy([1, 2, 2]) == 4
    assert candy([29, 51, 87, 87, 72, 12]) == 12
    assert candy([1, 6, 10, 8, 7, 3, 2]) == 18
    assert candy([1, 2, 3]) == 6
    assert candy([0, 1, 2, 5, 3, 2, 7]) == 15
    assert candy([0]) == 1


if __name__ == "__main__":
    main()

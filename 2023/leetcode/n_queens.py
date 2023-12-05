"""https://leetcode.com/problems/n-queens/"""


def main() -> None:
    test_update_available_positions()
    n = 4
    output = n_queens(n)
    expected_output = [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."]
    ]
    assert output == expected_output


def update_available_positions(available_positions: list[set[int]], queen_position: int):
    new_available_positions = []
    for i, positions in enumerate(available_positions[1:]):
        new_positions = set(positions)
        new_positions.discard(queen_position)
        new_positions.discard(queen_position-i-1)
        new_positions.discard(queen_position+i+1)
        new_available_positions.append(new_positions)
    return new_available_positions


def n_queens(n: int) -> list[list[str]]:
    solution = []

    def rec(current_line: int, available_positions: list[set[int]], building_solution: list[str]) -> None:
        if current_line < n:
            for position in available_positions[0]:
                left = "." * position
                right = "." * (n - position - 1)
                line = f"{left}Q{right}"
                new_building_solution = building_solution[:]
                new_building_solution.append(line)
                new_available_positions = update_available_positions(available_positions, position)
                rec(current_line+1, new_available_positions, new_building_solution)
        else:  # We have a solution if we reach current_line == n
            solution.append(building_solution)

    rec(0, [set(range(n)) for _ in range(n)], [])
    return solution


def test_update_available_positions() -> None:
    available_positions = [
        {0, 1, 2},
        {0, 1, 2},
        {0, 1, 2},
    ]
    queen_position = 0
    expected_available_positions = [
       #{0, 1, 2},
        {      2},
        {   1   },
    ]
    output = update_available_positions(available_positions, queen_position)
    assert output == expected_available_positions


if __name__ == "__main__":
    main()

"""4 - Your friend is developing a small image processing program
and has asked for your help in implementing MS-Paint's “paint bucket”-like
functionality. Their program represents images using arrays of characters,
with each array value representing a pixel and letters and symbols
representing different colors. For example, the following 4x6
matrix represents the letter P in color "#", with background color "." (dot)
.###..
.#..#.
.###..
.#....
"""


def paint_bucket(matrix, coord, new_color):
    x, y = coord
    adjacencies = get_valid_adjacencies(matrix, coord)
    matrix[x][y] = new_color
    for adj in adjacencies:
        paint_bucket(matrix, adj, new_color)
    return matrix


def check_valid_coord(matrix, coord):
    x, y = coord
    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
        return True
    return False


def get_valid_adjacencies(matrix, coord) -> set[tuple[int, int]]:
    x, y = coord
    valid_coords = set()
    # Assuming the valid coordinates to paint can be only the following:
    top = x - 1, y
    right = x, y + 1
    bottom = x + 1, y
    left = x, y - 1
    for coord in [top, right, bottom, left]:
        if check_valid_coord(matrix, coord):
            adjacent_color = matrix[coord[0]][coord[1]]
            color = matrix[x][y]
            if color == adjacent_color:
                valid_coords.add(coord)
    return valid_coords



def test_check_valid_coord(p_case) -> None:
    assert check_valid_coord(p_case, (0, 0)) is True
    assert check_valid_coord(p_case, (-1, 0)) is False
    assert check_valid_coord(p_case, (0, -1)) is False
    assert check_valid_coord(p_case, (len(p_case), 1)) is False
    assert check_valid_coord(p_case, (1, len(p_case[0]))) is False


def test_get_valid_adjacencies(p_case) -> None:
    assert get_valid_adjacencies(p_case, (0, 1)) == {(1, 1), (0, 2)}
    assert get_valid_adjacencies(p_case, (1, 3)) == {(1, 2)}
    assert get_valid_adjacencies(p_case, (2, 4)) == {(3, 4), (2, 5)}
    assert get_valid_adjacencies(p_case, (-1, -1)) == set()  # Invalid coord


def main() -> None:
    """Some test cases"""
    p_case = [
        [".", "#", "#", "#", ".", "."],
        [".", "#", ".", ".", "#", "."],
        [".", "#", "#", "#", ".", "."],
        [".", "#", ".", ".", ".", "."],
    ]
    test_check_valid_coord(p_case)
    test_get_valid_adjacencies(p_case)

    coord = (0, 1)
    new_color = "O"
    painted = paint_bucket(p_case, coord, new_color)
    assert painted == [
        [".", "O", "O", "O", ".", "."],
        [".", "O", ".", ".", "#", "."],
        [".", "O", "O", "O", ".", "."],
        [".", "O", ".", ".", ".", "."],
    ]

    p_case = [
        [".", "#", "#", "#", ".", "."],
        [".", "#", ".", ".", "#", "."],
        [".", "#", "#", "#", ".", "."],
        [".", "#", ".", ".", ".", "."],
    ]
    coord = (1, 3)
    new_color = "o"
    painted = paint_bucket(p_case, coord, new_color)
    assert painted == [
        [".", "#", "#", "#", ".", "."],
        [".", "#", "o", "o", "#", "."],
        [".", "#", "#", "#", ".", "."],
        [".", "#", ".", ".", ".", "."],
    ]

    p_case = [
        [".", "#", "#", "#", ".", "."],
        [".", "#", ".", ".", "#", "."],
        [".", "#", "#", "#", ".", "."],
        [".", "#", ".", ".", ".", "."],
    ]
    coord = (1, 3)
    new_color = "#"
    painted = paint_bucket(p_case, coord, new_color)
    assert painted == [
        [".", "#", "#", "#", ".", "."],
        [".", "#", "#", "#", "#", "."],
        [".", "#", "#", "#", ".", "."],
        [".", "#", ".", ".", ".", "."],
    ]


if __name__ == "__main__":
    main()

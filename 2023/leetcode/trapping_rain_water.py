# https://leetcode.com/problems/trapping-rain-water


def trap(height: list[int]) -> int:
    left_max = []
    right_max = []

    max_height_left = 0
    max_height_right = 0
    for elevation_left, elevation_right in zip(height, height[::-1]):
        left_max.append(max_height_left)
        right_max.append(max_height_right)
        max_height_left = max(max_height_left, elevation_left)
        max_height_right = max(max_height_right, elevation_right)

    right_max = right_max[::-1]

    flood = 0
    for i, elevation in enumerate(height):
        current_flood = min(right_max[i], left_max[i]) - elevation
        flood += current_flood if current_flood > 0 else 0

    return flood


def main() -> None:
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert trap(height) == 6


if __name__ == '__main__':
    main()


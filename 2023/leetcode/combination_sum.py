"""https://leetcode.com/problems/combination-sum"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    combinations = []
    sorted_candidates = list(sorted(candidates))

    def rec(candidates_: list[int], sum_: int, combination: list[int]) -> None:
        if candidates_:
            current_candidate = candidates_[0]
            current_sum = sum_ + current_candidate
            if current_sum == target:
                combination.append(current_candidate)
                combinations.append(combination)
            elif current_sum < target:
                rec(candidates_, current_sum, combination[:] + [current_candidate])
                rec(candidates_[1:], sum_, combination[:])
            elif current_sum > target:
                return

    rec(sorted_candidates, 0, [])
    return combinations


def main() -> None:
    candidates = [2, 3, 6, 7]
    target = 7
    output = combination_sum(candidates, target)
    print(output)


if __name__ == "__main__":
    main()

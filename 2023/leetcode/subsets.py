"""https://leetcode.com/problems/subsets"""


def subsets(nums: list[int]) -> list[list[int]]:
    sets = [[]]

    def rec(nums: list[int]):
        if len(nums) == 1:
            return
        else:
            new_combs = []
            for i, num in enumerate(nums):
                left = nums[:i]
                right = nums[i+1:]
                numbers = left + right
                if len(numbers) > 1:
                    sets.append(numbers)
                    rec(numbers)
            return new_combs

    rec(nums)
    sets.append(nums)
    for num in nums:
        sets.append([num])
    return sets


def main() -> None:
    nums = [1, 2, 3, 4]
    output = subsets(nums)
    print(output)


if __name__ == "__main__":
    main()

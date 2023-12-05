"""https://leetcode.com/problems/permutations"""


def permute(nums: list[int]) -> list[list[int]]:
    def perm(nums_: list[int]) -> list[list[int]]:
        if len(nums_) == 1:
            return [nums_]
        elif len(nums_) == 2:
            return [nums_, nums_[::-1]]
        else:
            new_perms = []
            n = len(nums_)
            for i in range(n):
                num = nums_[i]
                lefts = nums_[:i]
                rights = nums_[i+1:]
                perms = perm(lefts + rights)
                for p in perms:
                    new_perms.append([num] + p)
            return new_perms

    return perm(nums)


def main() -> None:
    nums = [1, 2, 3]
    output = permute(nums)


if __name__ == "__main__":
    main()

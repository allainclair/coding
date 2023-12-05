"""
Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Source: https://leetcode.com/problems/product-of-array-except-self/
"""


def main() -> None:
    test_1()
    test_2()


def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    products = [1]*len(nums)

    prod = 1
    for i, num in enumerate(nums[:-1]):
        prod *= num
        products[i+1] *= prod

    prod = 1
    for i, num in enumerate(nums[:0:-1]):  # Reversed back to 0.
        prod *= num
        products[n-i-2] *= prod

    return products


def test_1() -> None:
    nums = [1, 2, 3, 4]
    output = [24, 12, 8, 6]
    assert product_except_self(nums) == output


def test_2() -> None:
    nums = [-1, 1, 0, -3, 3]
    output = [0, 0, 9, 0, 0]
    assert product_except_self(nums) == output


if __name__ == "__main__":
    main()

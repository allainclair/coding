"""
https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.


Example 1:

Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 9
Output: 1
Explanation: Here there exists a subset with
sum = 9, 4+3+2 = 9.
Example 2:

Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 30
Output: 0
Explanation: There is no subset with sum 30.

Your Task:
You don't need to read input or print anything. Your task is to complete the function isSubsetSum() which takes the array arr[], its size N and an integer sum as input parameters and returns boolean value true if there exists a subset with given sum and false otherwise.
The driver code itself prints 1, if returned value is true and prints 0 if returned value is false.

Expected Time Complexity: O(sum*N)
Expected Auxiliary Space: O(sum*N)

Constraints:
1 <= N <= 100
1<= arr[i] <= 100
1<= sum <= 104
"""


def solve(set_, sum_):
	n = len(set_)
	set_ = [element for element in set_ if element <= sum_]
	d = {}
	for size in range(1, n+1):
		pass


def main():
	set_ = [3, 34, 4, 12, 5, 2]
	sum_ = 9
	print(solve(set_, sum_))


if __name__ == "__main__":
	main()

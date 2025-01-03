"""
https://www.geeksforgeeks.org/problems/path-in-matrix3805/1

Given a n x n matrix of positive integers. There are only three possible moves from a cell mat[r][c].

mat[r+1] [c]
mat[r+1] [c-1]
mat [r+1] [c+1]
Starting from any column in row 0 return the largest sum of any of the paths up to row n -1. Return the highest maximum path sum.

Note : We can start from any column in zeroth row and can end at any column in (n-1)th row.

Examples :

Input: n = 2, mat = [[348, 391],[618, 193]]
Output: 1009
Explaination: The best path is 391 -> 618. It gives the sum = 1009.

Input: n = 2, mat = [[2, 2],[2, 2]]
Output: 4
Explaination: No matter which path is chosen, the output is 4.
Expected Time Complexity: O(n * n)
Expected Auxiliary Space: O(n * n)
"""


def solve(mat):
	costs = [cost for cost in mat[0]]
	n = len(mat)

	for i in range(1, n):
		new = [0]*n
		for j in range(n):
			max_cost = costs[j] + mat[i][j]
			print(i, j)
			print("max_cost 1", max_cost)
			current_cost = mat[i][j]
			if j - 1 > -1 and max_cost < costs[j-1] + current_cost:
				max_cost = costs[j-1] + current_cost
				print("max_cost 2", max_cost)
			if j + 1 < n and max_cost < costs[j+1] + current_cost:
				max_cost = costs[j+1] + current_cost
				print("max_cost 3", max_cost)
			print("max_cost", max_cost)
			print(costs)
			new[j] = max_cost
			print(new)
			print()
		costs = new

	return max(costs)


def main():
	m = [[348, 391], [618, 193]]
	m = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
	m = [
		[10, 10, 10],
		[10, 1, 10],
		[1, 100, 1]
	]
	print(solve(m))


if __name__ == "__main__":
	main()


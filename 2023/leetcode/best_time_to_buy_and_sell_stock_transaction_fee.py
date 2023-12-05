"""
You are given an array prices where prices[i] is the price of a given stock
on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions
as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before you buy again).

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
"""


def main() -> None:
    test_1()
    test_2()


def bestbuy(prices: list[int], fee: int) -> int:
    n = len(prices)
    x0 = 0
    x1 = float('-inf')

    for i in range(n):
        x0 = max(x0, x1 + prices[i] - fee)
        x1 = max(x1, x0 - prices[i])
    return max(x0, x1)


def test_1() -> None:
    prices = [1, 3]
    fee = 1
    profit = bestbuy(prices, fee)
    assert profit == 1


def test_2() -> None:
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    profit = bestbuy(prices, fee)


if __name__ == '__main__':
    main()

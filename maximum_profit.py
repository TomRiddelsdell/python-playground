"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you
cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
from array import array


def maximum_profit(prices:array):
    if len(prices) <= 1:
        return 0

    min_level = prices[0]
    max_profit = 0

    for p in prices:
        if p < min_level:
            min_level = p

        if p - min_level > max_profit:
            max_profit = p - min_level

    return max_profit

def run_tests():
    assert maximum_profit([]) == 0
    assert maximum_profit([1]) == 0
    assert maximum_profit([1,1]) == 0
    assert maximum_profit([1,1]) == 0
    assert maximum_profit([1,2]) == 1
    assert maximum_profit([1,0,1]) == 1
    assert maximum_profit([3,2,1]) == 0
    assert maximum_profit([3,6,7]) == 4
    assert maximum_profit([1,2,0,2]) == 2
    assert maximum_profit([1,3,0,2]) == 2

run_tests()

"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
 

Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
 

Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""
from typing import List

def triangle(input:List[List[int]]) -> int:
    if len(input) == 0 or len(input[0]) != 1:
        return 0
    
    for row in range(len(input)-2, -1, -1):
        for i in range(len(input[row])):
            if input[row+1][i] < input[row+1][i+1]:
                input[row][i] += input[row+1][i]
            else:
                input[row][i] += input[row+1][i+1]

    return input[0][0]

def run_tests():
    assert triangle([[]]) == 0
    assert triangle([[1]]) == 1
    assert triangle([[1],[2,3]]) == 3
    assert triangle([[1],[2,3],[10,10,0]]) == 4

run_tests()
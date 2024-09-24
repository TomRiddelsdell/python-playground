"""
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.
A uni-value grid is a grid where all the elements of it are equal.
Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

Example 1:
Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.

Example 2:
Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.

Example 3:
Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
1 <= x, grid[i][j] <= 104

Thoughts:
2,4,6,8 -> 2
avg = 20/4 = 5
5 - 2 = 3
3 % 2 != 0
if remainer > x/2 round up otherwise round down
"""
from statistics import mean
from typing import List

def min_ops(grid:List[List[int]], x:int) -> int:
    shift = grid[0][0] % x
    shifted = []

    for sub in grid:
        for cell in sub:
            shifted.append(round((cell-shift)/x))

            if shifted[-1] != (cell-shift)/x:
                return -1

    tgt = round(mean(shifted))

    req_ops = 0

    for cell in shifted:
        req_ops += abs((cell-tgt)) 
        
    return req_ops

def run_tests():
    #assert min_ops([[2,4],[6,8]], 2) == 4
    #assert min_ops([[146]], 86) == 0
    #assert min_ops([[931,128],[639,712]], 73) == 12
    print(min_ops([[529,529,989],[989,529,345],[989,805,69]], 92) )

run_tests()
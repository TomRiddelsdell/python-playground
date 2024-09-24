"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""
def pascal(numRows):
    if numRows < 1:
        return []

    if numRows == 1:
        return([[1]])

    prev = pascal(numRows-1)
    lastRow = [0] + prev[-1] + [0]
    thisRow = [lastRow[i-1] + lastRow[i] for i in range(1,len(lastRow))]

    return prev + [thisRow]
        

def run_test():
    assert pascal(0) == []
    assert pascal(-1) == []
    assert pascal(1) == [[1]]
    assert pascal(2) == [[1],[1,1]]
    assert pascal(3) == [[1],[1,1],[1,2,1]]
    assert pascal(4) == [[1],[1,1],[1,2,1],[1,3,3,1]]
    assert pascal(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    
run_test()
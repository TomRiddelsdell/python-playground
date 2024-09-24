"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""
from math import log2


def count_bits_rec(input:int) -> list:
    if input == 0:
        return [0]
    
    nm1 = count_bits(input-1)
    if input % 2 == 1:
        return nm1 + [nm1[-1] + 1]

    decrement = -1
    while input % 2 == 0:
        decrement += 1
        input = input >> 1
    
    return nm1 + [nm1[-1]-decrement]

def count_bits(n:int) -> List[int]:
    dp = [0]
    for i in range(1,n+1):
        dp += 
        
    
def run_tests():
    assert count_bits(0) == [0]
    assert count_bits(1) == [0,1]
    assert count_bits(2) == [0,1,1]
    assert count_bits(3) == [0,1,1,2]
    assert count_bits(4) == [0,1,1,2,1]
    assert count_bits(16) == [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1]

run_tests()
x = [0]
x += [1]
print(x)
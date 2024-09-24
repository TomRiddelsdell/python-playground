"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to left.
The first integer of each row is greater than the last integer of the previous row.
"""

from ast import Raise
from tkinter import W
from typing import List
import bisect

class my_matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.m = len(self.matrix)
        if self.m > 0:
            self.n = len(self.matrix[0])
        else:
            self.n = 0

    def __getitem__(self, key):
        m_lookup = key // self.n 

        if m_lookup > self.m - 1:
            Raise("index out of bounds")

        n_lookup = key % self.n

        if n_lookup > self.n - 1:
            Raise("index out of bounds")

        return self.matrix[m_lookup][n_lookup]

def binary_search(mat, target:int, n:int) -> bool:
    if n == 0:
        return False
    
    last = n - 1
    first = 0

    while True:
        guess = (last + first) // 2

        if mat[guess] == target:
            return True
        
        if last == first:
            return False

        if mat[guess] > target:
            last = guess - 1
        else:
            first = guess + 1

def search_2d_old(matrix:List[List[int]], target:int) -> bool:
    mat = my_matrix(matrix) 
    return binary_search(mat, target, mat.n * mat.m)

def search_2d(matrix:List[List[int]], target:int) -> bool:
    n = len(matrix)
    if n == 0 or len(matrix[0]) == 0:
        return False

    n_loc = bisect.bisect_left(matrix, target, key=lambda x: x[0])

    if n_loc < n and matrix[n_loc][0] == target:
        return True

    m_loc = bisect.bisect_left(matrix[n_loc-1], target)
    return m_loc < len(matrix[n_loc-1]) and matrix[n_loc-1][m_loc] == target

def run_tests():
    #assert my_matrix([[0]])[0] == 0
    #assert my_matrix([[0,1]])[1] == 1
    #assert my_matrix([[0,1],[2,3]])[2] == 2
    #assert my_matrix([[0,1],[2,3]])[3] == 3
    assert search_2d([],0) == False
    assert search_2d([[1]],0) == False
    assert search_2d([[1]],1) == True
    assert search_2d([[],[]],1) == False
    assert search_2d([[2,3,4]],1) == False
    assert search_2d([[2,3,4]],2) == True
    assert binary_search([2,3,4],4,3) == True
    assert search_2d([[2,3,4]],4) == True
    assert search_2d([[2,3,4],[5,6,7]],4) == True
    assert search_2d([[2,3,4],[6,6,7]],5) == False
    assert search_2d([[2,3,4],[6,6,7]],6) == True

run_tests()
#print(search_2d([[2,3,4],[6,6,7]],6))
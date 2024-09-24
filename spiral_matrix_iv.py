"""
You are given two integers m and n, which represent the dimensions of a matrix.
You are also given the head of a linked list of integers.
Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.
Return the generated matrix.

Example 1:
Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.
Example 2:

Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.
 
Constraints:
1 <= m, n <= 105
1 <= m * n <= 105
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000
"""
# Definition for singly-linked list.
from email.header import make_header
from email.utils import make_msgid
from platform import mac_ver
from typing import List, Optional
import numpy as np

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pop_head(self,head:ListNode) -> int:
        if head is None:
            return -1, None

        return head.val,head.next
    
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-2]*n for x in range(m)]
        col_start = 0
        col_end = n-1
        row_start = 0
        row_end = m-1

        while True:
            if col_end < col_start:
                break

            for i in range(col_start, col_end+1):
                result[row_start][i], head = self.pop_head(head)

            row_start +=1
            
            if row_start > row_end:
                break

            for j in range(row_start,row_end+1):
                result[j][col_end], head = self.pop_head(head)
                
            col_end -= 1

            if col_end < col_start:
                break
            
            for i in range(col_end, col_start-1, -1):
                result[row_end][i], head = self.pop_head(head)

            row_end -= 1
            if row_end < row_start:
                break
                
            for j in range(row_end, row_start-1, -1):
                result[j][col_start], head = self.pop_head(head)

            col_start += 1


        return result        
        
def list_to_ll(list:List[int]) -> Optional[ListNode]:
    if len(list) == 0:
        return None

    cur = head = ListNode(list[0])
    for x in list[1:]:
        cur.next = ListNode(x)
        cur = cur.next

    return head

def ll_to_list(ll:Optional[ListNode]):
    ret = []
    while ll is not None:
        ret.append(ll.val)
        ll = ll.next
    
    return ret
    
sol = Solution()
res = sol.spiralMatrix(9, 6, list_to_ll([995,348,36,516,333,627,248,422,13,225,764,311,405,695,698,83,145,783,478]))
print(np.array(res))


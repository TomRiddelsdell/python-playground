"""
Given an n-ary tree, return the level order traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

Constraints:
The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 104]
"""
from queue import Queue
from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        to_search = Queue()
        current_depth = root.depth = 0
        to_search.put(root)
        
        output = []
        current_level = []
        
        while not to_search.empty():
            next_node = to_search.get()
            
            if next_node.depth > current_depth:
                output.append(current_level)
                current_depth += 1
                current_level = []
                
            current_level.append(next_node.val)
            
            for child in next_node.children:
                child.depth = current_depth + 1
                to_search.put(child)
                
        output.append(current_level)
        
        return output
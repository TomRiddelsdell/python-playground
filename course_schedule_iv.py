"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.

 

Example 1:


Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.
Example 2:

Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites, and each course is independent.
Example 3:


Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]
 

Constraints:

2 <= numCourses <= 100
0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
prerequisites[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
All the pairs [ai, bi] are unique.
The prerequisites graph has no cycles.
1 <= queries.length <= 104
0 <= ui, vi <= n - 1
ui != vi
"""

from tkinter import W
from typing import Dict, List, Set
from queue import Queue
import numpy as np

def is_prerequisite(candidate:int, of:int, tree:Dict[int,Set[int]]) -> bool:
    to_traverse = Queue()
    to_traverse.put(of)
    
    while not to_traverse.empty():
        cur = to_traverse.get()
        
        if cur in tree:
            for sub_pre in tree[cur]:
                if sub_pre == candidate:
                    return True
                to_traverse.put(sub_pre)

    return False

def build_tree(prerequisites:List[List[int]]) -> Dict[int,Set[int]]: 
    pre = dict()   
    for x in prerequisites:
        if x[1] in pre:
            pre[x[1]].add(x[0])
        else:
            pre[x[1]] = {x[0]}

    return pre
    
def build_floyde_warshall_matrix(n:int, prerequisites:List[List[int]]) -> np.ndarray:
    dist = np.zeros((n,n))

    for [prereq,of] in prerequisites:
        dist[prereq,of] = 1

    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i,k] and dist[k,j]:
                    dist[i,j] = 1

    return dist

def is_prerequisite_from_matrix(prereq_candidate:int, of:int, dist:List[List[int]]) -> bool:
    return dist[prereq_candidate, of]

def prerequisites(numCourses:int, prerequisites:List[List[int]], queries:List[List[int]]) -> List[int]:
    if numCourses < 2:
        return False

    dist_matrix = build_floyde_warshall_matrix(numCourses, prerequisites)
    res = []
    
    for [x,y] in queries:
        if is_prerequisite_from_matrix(x, y, dist_matrix):
            res.append(True)
        else:
            res.append(False)

    return res

def run_tests():
    assert np.array_equal(build_floyde_warshall_matrix(2, [[0,1]]), np.array([[0, 1], [0, 0]]))
    assert prerequisites(2, [[1,0]], [[0,1],[1,0]]) == [False, True]
    assert prerequisites(4, [[2,3],[2,1],[0,3],[0,1]], [[0,1],[0,3],[2,3],[3,0],[2,0],[0,2]]) == [True,True,True,False,False,False]
    assert prerequisites(5, [[0,1],[1,2],[2,3],[3,4]], [[0,4],[4,0],[1,3],[3,0]]) == [True,False,True,False]

run_tests()

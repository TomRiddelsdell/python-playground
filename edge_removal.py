'''Task:
You are given an undirected graph represented by its adjacency list. The graph may contain isolated vertices (vertices with no edges). At each second, you remove vertices that have fewer than one neighbor (order 1) and any corresponding edges. Your goal is to find the number of seconds it takes until no such vertices remain in the graph.

Write a function solution(N, edges) that, given an integer N representing the number of vertices in the graph and a list of tuples edges 
representing the edges of the graph, returns the minimum number of seconds required to remove all vertices with order 1 and their 
corresponding edges.

Examples:
Given 
N=6 and edges = [(1, 2), (2, 3), (2, 4), (4, 5), (4, 6)], the function should return 2.Explanation: Initially, vertices 1, 3, 5, and 6
have order 1. After the first second, vertices 1 and 3, along with their corresponding edges, are removed. After the second second, 
vertices 5 and 6, along with their corresponding edges, are removed. No vertices with order 1 remain in the graph.

Given N=5 and edges = [(1, 2), (2, 3), (2, 4)], the function should return 1.Explanation: Initially, vertices 1, 3, and 4 have order 1. 
After the first second, vertices 1, 3, and 4, along with their corresponding edges, are removed. No vertices with order 1 remain in the 
graph.

Constraints:
1 ≤ 𝑁 ≤ 1 0 5
1≤N≤10 5 
0 ≤ len ( 𝑒 𝑑 𝑔 𝑒 𝑠) ≤ 1 0 5 
0≤len(edges)≤10 5
 
This problem involves graph traversal and manipulation. You may want to use techniques like breadth-first search (BFS) to iteratively 
remove vertices with order 1 until no such vertices remain. Additionally, you'll need to efficiently handle the removal of edges from 
the adjacency list during each iteration.
'''

def solution(N, edges):
    counts = {}

    for i in range(1, N + 1):
        counts[i] = 0

    for (from_v, to_v) in edges:
        counts[from_v] = counts.get(from_v) + 1
        counts[to_v] = counts.get(to_v) + 1

    seconds = 0

    while True:
        to_remove = []
        for v, order in counts.items():
            if order <= 1:
                to_remove.append(v)

        if len(to_remove) == 0:
            break

        for v in to_remove:
            del counts[v]

        for (from_v, to_v) in edges:
            if from_v in to_remove or to_v in to_remove:
                if from_v in counts: counts[from_v] -= 1
                if to_v in counts: counts[to_v] -= 1
        
        seconds += 1

    return seconds

def run_tests():
    assert solution(6, [(1, 2), (2, 3), (2, 4), (4, 5), (4, 6)]) == 2
    assert solution(6, [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6)]) == 2
    assert solution(5, [(1, 2), (2, 3), (2, 4)]) == 2
    assert solution(5, [(1, 2), (2, 3), (3, 4),(4, 5)]) == 3
    assert solution(5, [(1, 2), (2, 3), (3, 4),(4, 1)]) == 1
    assert solution(4, [(1, 2), (2, 3), (3, 4),(4, 1)]) == 0
    assert solution(5, []) == 1
    assert solution(1, [(1,1)]) == 0

run_tests()
print("Success")


from collections import defaultdict

def solution2(N, edges):
    graph = defaultdict(set)
    degree = defaultdict(int)

    for i in range(1, N + 1):
        graph[i] = set()
        degree[i] = 0

    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
        degree[u] += 1
        degree[v] += 1

    queue = [node for node in degree if degree[node] <= 1]
    max_depth = 0

    while True:
        if len(queue) == 0:
            break

        max_depth += 1
        N -= len(queue)
        new_queue = []
        for node in queue:
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    new_queue.append(neighbor)
        queue = new_queue

    return max_depth


def run_tests2():
    assert solution2(6, [(1, 2), (2, 3), (2, 4), (4, 5), (4, 6)]) == 2
    assert solution2(6, [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6)]) == 2
    assert solution2(5, [(1, 2), (2, 3), (2, 4)]) == 2
    assert solution2(5, [(1, 2), (2, 3), (3, 4),(4, 5)]) == 3
    assert solution2(5, [(1, 2), (2, 3), (3, 4),(4, 1)]) == 1
    assert solution2(4, [(1, 2), (2, 3), (3, 4),(4, 1)]) == 0
    assert solution2(5, []) == 1

run_tests2()
print("Success2")
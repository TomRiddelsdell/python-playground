"""
You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.
We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.
Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.
Return the largest possible overlap.

Example 1:
Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.
The number of positions that have a 1 in both images is 3 (shown in red).

Example 2:
Input: img1 = [[1]], img2 = [[1]]
Output: 1
Example 3:

Input: img1 = [[0]], img2 = [[0]]
Output: 0

Constraints:
n == img1.length == img1[i].length
n == img2.length == img2[i].length
1 <= n <= 30
img1[i][j] is either 0 or 1.
img2[i][j] is either 0 or 1.
"""
from typing import List

def overlap(img1:List[List[int]], img2:list[List[int]]) -> int:
    n = len(img1)
    result = 0

    for i in range(n):
        for j in range(n):
            if img1[i][j] and img2[i][j]:
                result += 1
                
    return result

def apply_shift(img:List[List[int]], right, down) -> List[List[int]]:
    n = len(img)

    # down shift
    if down > 0:
        img = [[0]*n for i in range(down)] + img[0:-down-1]
    elif down < 0:
        img = img[-down:] + [[0]*n for i in range(-down)]

    # right shift
    if right > 0:
        for i in range(n):
            img[i] = [0]*right + img[i][:-right-1]
    elif right < 0:
        for i in range(n):
            img[i] = img[i][-right:] + [0]*(-right)

    return img

def max_overlap(img1:List[List[int]], img2:List[List[int]]) -> int:
    best_right = 0
    best_left = 0
    best_overlap = 0
    n = len(img1)

    for cur_right in range(-n+1, n):
        for cur_down in range(-n+1, n):
            cur_overlap = overlap(img1, apply_shift(img2, cur_right, cur_down))
            
            if cur_overlap > best_overlap:
                best_overlap = cur_overlap
                best_right = cur_right
                best_left = cur_down

    return best_overlap

def run_tests():
    assert max_overlap([],[]) == 0
    assert max_overlap([[1]],[[1]]) == 1
    assert max_overlap([[0]],[[1]]) == 0
    assert max_overlap([[0,1],[0,0]],[[1,0],[0,0]]) == 1
    assert max_overlap([[0,0],[1,0]],[[1,0],[0,0]]) == 1

#run_tests()
print(max_overlap([[0,1],[0,0]],[[1,0],[0,0]]))
"""
You are given two positive integer arrays nums1 and nums2, both of length n.

The absolute sum difference of arrays nums1 and nums2 is defined as the sum of |nums1[i] - nums2[i]| for each 0 <= i < n (0-indexed).

You can replace at most one element of nums1 with any other element in nums1 to minimize the absolute sum difference.

Return the minimum absolute sum difference after replacing at most one element in the array nums1. Since the answer may be large, return it modulo 109 + 7.

|x| is defined as:

x if x >= 0, or
-x if x < 0.
 

Example 1:

Input: nums1 = [1,7,5], nums2 = [2,3,5]
Output: 3
Explanation: There are two possible optimal solutions:
- Replace the second element with the first: [1,7,5] => [1,1,5], or
- Replace the second element with the third: [1,7,5] => [1,5,5].
Both will yield an absolute sum difference of |1-2| + (|1-3| or |5-3|) + |5-5| = 3.
Example 2:

Input: nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
Output: 0
Explanation: nums1 is equal to nums2 so no replacement is needed. This will result in an 
absolute sum difference of 0.
Example 3:

Input: nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
Output: 20
Explanation: Replace the first element with the second: [1,10,4,4,2,7] => [10,10,4,4,2,7].
This yields an absolute sum difference of |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20
 

Constraints:

n == nums1.length
n == nums2.length
1 <= n <= 105
1 <= nums1[i], nums2[i] <= 105

Working:
[1,10,4,4,2,7]
[9,3,5,1,7,4]

1. calc abs diffs [8,7,1,3,5,3] o(n)
2. find index i of min o(n)
3. find element x in nums1 which is closest to nums2[i] o(n)
4. replace nums1[i] with x o(1) -> this is an incorrect assumption
5. recalculate abs diff[i] o(1)
6. calc the sum of the abs diffs o(n)

Brute force:
1. Calculate all combinations for nums1 after replacement o(n^2)
2. calc sum abs diff for each o(n^3)
3. find the min o(n^2)

i = element to replace
j = element to replace with
replacement saving = |nums1[j]-nums2[i]| - |nums1[i]-nums2[i]|
replacement saving = |nums1[j] - nums1[i]|
"""
import bisect
from typing import List

def best_replacements(nums1:List[int], nums2:List[int]) -> List[int]:
    best_replace = nums1[:]
    nums1_sorted = sorted(nums1) #nlogn

    for i in range(len(nums1)):
        i_sorted = bisect.bisect_left(nums1_sorted, nums2[i])
        if i_sorted == len(nums1):
            best_replace[i] = nums1_sorted[i_sorted-1]
        elif i_sorted > 0 and abs(nums1_sorted[i_sorted-1] - nums2[i]) < abs(nums1_sorted[i_sorted] - nums2[i]):
            best_replace[i] = nums1_sorted[i_sorted-1]
        else:
            best_replace[i] = nums1_sorted[i_sorted]
    
    return best_replace

def array_with_max_gain(nums1:List[int], nums2:List[int], best_replace:List[int]) -> List[int]:
    max_gain = 0
    max_gain_idx = 0

    for i in range(len(nums1)):
        gain = abs(nums1[i]-nums2[i]) - abs(best_replace[i]-nums2[i])
        if gain > max_gain:
            max_gain = gain
            max_gain_idx = i

    nums1_opt = nums1[:]
    nums1_opt[max_gain_idx] = best_replace[max_gain_idx]

    return nums1_opt

def sum_max_diff(nums1:List[int], nums2:List[int]) -> int:
    total = 0
    base = int(1e9 + 7)
    for (x,y) in zip(nums1, nums2):
        total = (total + abs(x-y)%base) % base

    return total

def min_diff(nums1:List[int], nums2:List[int]) -> int:
    if len(nums1) < 2:
        return sum_max_diff(nums1, nums2)
        
    best_replace = best_replacements(nums1,nums2)
    nums1_opt = array_with_max_gain(nums1, nums2, best_replace)

    return sum_max_diff(nums1_opt, nums2)

def run_tests():
    assert min_diff([],[]) == 0
    assert min_diff([1],[1]) == 0
    assert min_diff([1],[2]) == 1
    assert min_diff([2],[1]) == 1
    #assert min_diff([1],[-2]) == 1
    #assert min_diff([1],[1,2]) == ?
    assert min_diff([2,1],[10,1]) == 8
    assert min_diff([2,1],[10,2]) == 8
    assert min_diff([1,10,4,4,2,7], [9,3,5,1,7,4]) == 20
    
run_tests()
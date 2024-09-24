"""
You are given an integer array nums. You are initially positioned at the
array's first index, and each element in the array represents your maximum 
jump length at that position.

Return true if you can reach the last index, or false otherwise.


Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
jump length is 0, which makes it impossible to reach the last index.

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""
import matplotlib.pyplot as plt

def can_reach_end(nums:list):
    if len(nums) <= 1:
        return True

    idx = len(nums)-1
    while idx > 0:
        for from_end in range(1, idx+1):
            if nums[idx - from_end] >= from_end:
                idx -= from_end
                break

        if from_end == len(nums):
            return False
       
    return False

def run_tests():
    assert can_reach_end([]) is True
    assert can_reach_end([0]) is True
    assert can_reach_end([1]) is True
    assert can_reach_end([0,1]) is False
    assert can_reach_end([1,1]) is True
    assert can_reach_end([2,0,0]) is True
    assert can_reach_end([1,1,0]) is True

run_tests()

plt.plot([1, 2, 3, 50])
plt.ylabel('some numbers')
mngr = plt.get_current_fig_manager()
mngr.canvas.manager.window.wm_geometry("+1200+0") #right-hand side

plt.show()
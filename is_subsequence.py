"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""

def sub_sequence(outer:str, inner:str) -> bool:
    if len(inner) == 0:
        return True

    if len(outer) == 0:
        return False
    
    if inner[0] != outer[0]:
        return sub_sequence(outer[1:], inner)

    return sub_sequence(outer[1:], inner[1:])

def run_tests():
    assert sub_sequence("","") == True
    assert sub_sequence("","a") == False
    assert sub_sequence("a","a") == True
    assert sub_sequence("ab","a") == True
    assert sub_sequence("acb","ab") == True
    assert sub_sequence("acb","ba") == False
    assert sub_sequence("ahbgdc","axc") == False
    assert sub_sequence("ahbgdc","abc") == True

run_tests()
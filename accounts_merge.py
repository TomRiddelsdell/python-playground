"""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Example 2:
Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

Constraints:
1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
"""
from typing import Dict, List


def has_overlapping_email(a:List[str], b:List[str]) -> bool:
    a_i = 0
    b_i = 0
    
    while a_i < len(a) and b_i < len(b):
        if a[a_i] == b[b_i]:
            return True
        
        if a[a_i] > b[b_i]:
            b_i += 1
        else:
            a_i += 1
    
    return False

def merge_emails(a:List[str], b:List[str]) -> List[str]:
    result = []

    a_i = 0
    b_i = 0
    
    while a_i < len(a) or b_i < len(b):
        if a_i >= len(a):
            if len(result)==0 or result[-1] != b[b_i]:
                result.append(b[b_i])
            b_i += 1
        elif b_i >= len(b):
            if len(result)==0 or result[-1] != a[a_i]:
                result.append(a[a_i])
            a_i += 1
        else:
            if a[a_i] < b[b_i]:
                if len(result)==0 or result[-1] != a[a_i]:
                    result.append(a[a_i])
                a_i += 1
            else:
                if len(result)==0 or result[-1] != b[b_i]:
                    result.append(b[b_i])
                b_i += 1
    
    return result 
        
def merge_accs_for_name(accounts:List[List[str]]) -> List[List[str]]:
    accounts = [sorted(acc) for acc in accounts ]
    
    n = len(accounts)
    to_merge = []
    
    for i in range(n):
        for j in range(i+1, n):
            if has_overlapping_email(accounts[i], accounts[j]):
                to_merge.append([i,j])
                
    for i in range(len(to_merge)):
        accounts[to_merge[i][0]] = merge_emails(accounts[to_merge[i][0]], accounts[to_merge[i][1]])
        accounts[to_merge[i][1]] = None
        for j in range(len(to_merge)):
            if to_merge[j][0] == to_merge[i][1]:
                to_merge[j][0] = to_merge[i][0]
            if to_merge[j][1] == to_merge[i][1]:
                to_merge[j][1] = to_merge[i][0]
                
    return [x for x in accounts if not x is None]
    
def build_name_to_accs(accounts:List[List[str]]) -> Dict[str,List[List[str]]]:
    result = {}

    for acc in accounts:
        if acc[0] in result:
            result[acc[0]].append(acc[1:])
        else:
            result[acc[0]] = [acc[1:]]

    return result
    
def merged_accs(accounts:List[List[str]]) -> List[List[str]]:
    name_to_accs = build_name_to_accs(accounts)
    result = []

    for name, candidate_accs in name_to_accs.items():
        merged = merge_accs_for_name(candidate_accs)

        for merged_acc in merged:
            result.append([name] + merged_acc)

    return result

def run_tests():
    assert merged_accs([]) == []
    assert merged_accs([["Tom", "email1"]]) == [["Tom", "email1"]]
    assert merged_accs([["Tom", "email2", "email1"]]) == [["Tom", "email1", "email2"]]
    assert merged_accs([["Tom", "email2", "email1"],["Jo", "j1", "j2"]]) == [["Tom", "email1", "email2"],["Jo", "j1", "j2"]]
    assert merged_accs([["Tom", "email2", "email1"],["Tom", "j1", "j2"]]) == [["Tom", "email1", "email2"],["Tom", "j1", "j2"]]
    assert merged_accs([["Tom", "email2", "email1"],["Tom", "j1", "email1"]]) == [["Tom", "email1", "email2", "j1"]]

run_tests()
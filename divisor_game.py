"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.

Example 1:

Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: n = 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 
Constraints:

1 <= n <= 1000
"""

def divisor_game(n:int) -> bool:
    if n == 1:
        return False
    
    divisors = [x for x in range(int(n/2),0,-1) if n % x == 0]

    for div in divisors:
        if not divisor_game(n-div):
            return True

    return False    

def run_tests():
    assert divisor_game(1) == False
    assert divisor_game(2) == True
    assert divisor_game(3) == False
    assert divisor_game(4) == True
    assert divisor_game(5) == False
    assert divisor_game(6) == True
    assert divisor_game(7) == False
    assert divisor_game(8) == True
    assert divisor_game(9) == False
    assert divisor_game(10) == True
    assert divisor_game(11) == False
    assert divisor_game(12) == True

run_tests()
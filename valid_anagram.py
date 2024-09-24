def is_anagram(s:str, t:str) -> bool:
    if len(s) != len(t) or len(t) == 0:
        return False

    pos_of_t0_in_s = s.find(t[0])
    
    if pos_of_t0_in_s == -1:
        return False
    
    return True
    
def run_tests():
    assert is_anagram("", "") is True
    assert is_anagram("a", "") is False
    assert is_anagram("a", "b") is False
    assert is_anagram("ab", "ba") is True

run_tests()
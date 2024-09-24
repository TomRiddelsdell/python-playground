'''
2 bins of size b1 and b2. 
n items of size n1, n2, ...

find the maximum number of items that can be packed into the 2 bins 
'''

def solution(b1, b2, n):
    arrangements = 2**len(n)
    items = sorted(n)
    best_result = 0

    for test in range(arrangements):
        bin1 = []
        bin2 = []
        bin1_sum = 0
        bin2_sum = 0
        added = False
        
        for i in range(len(n)):
            if test & (1 << i):
                if(bin1_sum + n[i] <= b1):
                    bin1.append(n[i])
                    bin1_sum += n[i]
                    added = True
            else:
                if(bin2_sum + n[i] <= b2):
                    bin2.append(n[i])
                    bin2_sum += n[i]
                    added = True

            if not added:
                test_result = i-1
                if test_result > best_result:
                    best_result = test_result
                
                print(f"bin1={bin1}, bin2={bin2}, test_result={test_result}")
                continue

    return best_result

def run_tests():
    assert solution(3, 3, [1, 2, 3, 4] ) == 3
    assert solution(3, 3, [1, 2, 3, 2, 1] ) == 4
    assert solution(3, 3, [] ) == 0
    assert solution(0, 3, [1, 1, 1, 1] ) == 3
    assert solution(0, 3, [2, 2, 1, 1, 1, 1]) == 3
    assert solution(3, 0, [1, 1, 1, 1]) == 3
    assert solution(3, 0, [2, 2, 1, 1, 1, 1]) == 3

run_tests()
print("Success")
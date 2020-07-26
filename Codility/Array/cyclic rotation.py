def solution(A, K):
    result = [None] * len(A)
    for i in range(len(A)): 
        print(len(A))
        result[(i + K) % len(A)] = A[i]
    return result


A = [1, 2, 3, 4, 5]
K = 2
print(solution(A, K))

'''
Short Problem Definition:
Find an index of an array such that its value occurs at more than half of indices in the array.

Link
Dominator

Complexity:
expected worst-case time complexity is O(N);

expected worst-case space complexity is O(1)
>>> what interd in my mind i will use hash table but it is better because the space complexity will be O(N)

'''

A=[5,5,3,5,5,10,6,5,5,9,2,0]
# time complexity is O(N)  |  space complexity is O(1)
def solution(A):
    candidate_ele = ''
    candidate_cnt = 0

    for value in A:
        if candidate_ele == '':
            candidate_ele = value
            candidate_cnt = 1
        else:
            if value != candidate_ele:
                candidate_cnt -= 1
                if candidate_cnt == 0:
                    candidate_ele = ''
            else:
                candidate_cnt += 1

    if candidate_cnt == 0:
        return False

    cnt = 0
    last_idx = 0

    for idx, value in enumerate(A):
        if value == candidate_ele:
            cnt += 1
            last_idx = idx

    if cnt > len(A) // 2:
        return last_idx

    return False
print(solution(A))
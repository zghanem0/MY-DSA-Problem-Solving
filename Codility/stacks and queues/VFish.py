# Time O(N) | Space O(1)
# for that Solution i'm using p as an opposite fish and q is the other fish that come towards the opposite fish
#
def VFish(A, B):
    opp_fish = 0
    remaining = 0
    p = 0
    q = 0
    while True:
        if q > len(A) - 1 or p > len(A) - 1:
            break
        if opp_fish == 0:
            if B[p] == 0:
                remaining += 1
                p+=1
                continue
            else:
                opp_fish += 1

        q = p + 1
        while A[p] > A[q]:
            q += 1
        remaining+=1
        opp_fish -= 1
        p = q + 1

    return remaining


A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
print(VFish(A, B))


#A = [1,2,3,2]
A = [16,17,4, 2, 3,2, 4,9, 2, 6, 8,13]
#A=[1,2,3,2,5,6]
#A=[2,2]
def BiValued(A):
    dic={}
    current_bivalued=0
    longest_bivalued=0

    for i in A:
        if i in dic:
            dic[i]=1
        else:
            dic[i]=0
    for a in A:
        if dic[a]==1:
            current_bivalued += 1
            longest_bivalued=max(current_bivalued,longest_bivalued)
        elif longest_bivalued==0:
            continue
        else:
            current_bivalued+=1
        print(current_bivalued, longest_bivalued)

    return longest_bivalued
print(BiValued(A))






# ------------------------------- another one with dic -------------------------------------------------------------



#A = [1,2,3,2]
A=[4,2,2,4,2,6,8]
#A=[1,2,3,2,5,6]
#A=[2,2]
def BiValued(A):
    dic = {}
    LongestBiValued = 0
    temp_LongestBiValued=0
    for a in A:
        if a in dic:
            dic[a]=1
        else:
            dic[a]=0
    for a in A:
        if temp_LongestBiValued>=1:
            temp_LongestBiValued+=1
        if dic[a]==1 :
            if LongestBiValued ==0:
                temp_LongestBiValued=LongestBiValued=1
            else:
                LongestBiValued= temp_LongestBiValued
    return LongestBiValued


print(BiValued(A))

# --------------------------- other prety awsome solution with array ------------------------

# A = [1,2,3,2]
#A = [4, 2, 2, 4, 2, 6, 8]
A=[1,2,3,2,5,6]
#A=[2,2]
def BiValued(A):
    dic = {}
    i = 0
    j = len(A) - 1

    for a in A:
        if a in dic:
            dic[a] = 1
        else:
            dic[a] = 0
    while i < j:
        print(i,j)
        if dic[A[i]] == 1 and dic[A[j]] == 1 :
            break

        elif dic[A[i]] == 1:
            j -= 1
            continue

        elif dic[A[j]] == 1:
            i += 1
            continue
        else:
            i+=1
            j-=1
    size = (j-i+1)
    return size
print(BiValued(A))

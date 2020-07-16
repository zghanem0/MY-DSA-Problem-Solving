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

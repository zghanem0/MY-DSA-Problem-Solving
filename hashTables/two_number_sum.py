arr=[-14,5,-4,8,-11,1,-1,6,2,5,7,6]
k=10

def twosum(arr,k):
    nums= {}
    for num in arr:
        y=k-num
        if y in nums:
            print([y,num])
        else :
            nums[num]=True
    return nums

print(twosum(arr,k))
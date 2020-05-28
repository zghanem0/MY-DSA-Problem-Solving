sent = "aaabb"
def compress(s):
    r=""
    l=len(s)
    if l==0:
        print("")
    if l==1:
        print(s+"1")

    cnt=1
    i=1

    while i<l :
        if s[i]==s[i-1]:
            cnt+=1
        else:
            r=r+s[i-1]+str(cnt) # count the previous (i) not the curent "i", end the previouse compress
            cnt=1  # zero the count for the next iter
            print(r,s[i-1],cnt)

        i+=1
    r=r+s[i-1]+str(cnt)  # that out of loop but calc for the last loop
    print(r)

compress(sent)
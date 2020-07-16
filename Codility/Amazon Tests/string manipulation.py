import re
def solution(S):
    larger=0

    S=re.split('\.|\*|\?|!', S)
    print(S)
    for sent in S:
        temp_word_sent=sent.split()
        temp_sum=len(temp_word_sent)
        larger=max(larger,temp_sum)
    return larger

S = "we test. coders! Give us a try?"
print(solution(S))
#print(re.split('\.|\*|\?|!', S))

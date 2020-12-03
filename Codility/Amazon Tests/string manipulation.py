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


# Another Solution by unifing the delimiters: using replace method : replace word by word >> <sentance>.replace('old-word','new-word') 

def solution(S):
    larger=0
    replace1=S.replace('?','!')
    replace2=replace1.replace('.','!')
    sentence=replace2.split('!')
    print(sentence)
    for sent in sentence:
        splited_sent=sent.split()
        words_count=len(splited_sent)
        larger=max(larger,words_count)
    return larger

S = "we test. coders! Give us a try?"
print(solution(S))

def LongestWord(sen):
    temp_word = ""
    longest_word = ""
    for i in sen:
        # print(longest_word,temp_word)
        if i.isalnum():
            temp_word += i
        else:
            temp_word += " "
        print(temp_word.split())
  # code goes here
    return max(temp_word.split(), key=len)


# keep this function call here
print(LongestWord("I love dogs"))

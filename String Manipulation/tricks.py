# split at multiple delimiter
word = "ahmed_ghanem/is-happy"
folder = word.replace('/', '_').split("_")
print(folder)


# max() method can accept iterable as a parameter and function as an optional parameter key paramter u can pass the function that will get the max depends on it
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
    # u an array get the maximum of this array based on the len
    return max(temp_word.split(), key=len)


# keep this function call here
print(LongestWord("I love dogs"))

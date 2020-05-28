'''sent = "  ahmed ghanem"


def rev_words(s):  # to create a split() function manually
    words = []
    space = " "
    length = len(s)
    print(len(s))
    i = 0

    while i < length:
        if s[i] not in space: # to sure if the char is white space or not
            word_start = i  # to create the word start
            print(i)
            while i < length and s[i] not in space: # to split a word from the whole sentence and create the (word_end)
                i += 1

            words.append(s[word_start:i])
        i += 1
    print(words)
    print(" ".join(reversed(words)))

rev_words(sent)
'''

# ********************* using python trick (not recommended in the interview) **********************
sent2="ahmed ghanem  "
def rev_words2(s):
     print(" ".join(reversed(s.split())))  # split the sentence into splited words but start from the last and join them

rev_words2(sent2)
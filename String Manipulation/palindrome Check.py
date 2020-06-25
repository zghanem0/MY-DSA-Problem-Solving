string = "abcdcba"

def palindrome_check(str):
    counter = 0
    for i in range(len(str) - 1):
        end = len(str) - 1 - counter
        if i == end:
            if str[i] == str[end]:
                return True
        if str[i] != str[end]:
            return False
        counter += 1


print(palindrome_check(string))
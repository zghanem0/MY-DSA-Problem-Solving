def MathChallenge(x):
    num, cnt = 2, 0  # while cnt is the number of prime numbers that "while loop" found and num is the number of the number he checked as he will gonna check from 2 but he will add n+=1 that is was intiated with 1 not 2
    while True:
        if is_prime(num):
            cnt = cnt + 1
            if cnt == x:
                return num
        num = num + 1


def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
    # keep this function call here


print(MathChallenge(100))

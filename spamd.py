import random 


def spamm(long):
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    spamh = ''
    long = random.randint(5, 6)
    for i in range(long):
        spamh += random.choice(char)
    return spamh

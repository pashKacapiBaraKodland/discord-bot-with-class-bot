import random 


def spamm():
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    spamh = ''
    long = random.randint(5, 60)
    for i in range(long):
        spamh += random.choice(char)
    return spamh

def minion_game(string):
    vowels = 'AEIOU'
    k_score = 0
    s_score = 0
    for i in range(len(string)):
        if string[i] in vowels:
            k_score += (len(string)-i)
        else:
            s_score += (len(string)-i)

    if k_score > s_score:
        print ("Kevin {}".format(k_score))
    elif kevsc < stusc:
        print ("Stuart {}".format(s_score))
    else:
        print ("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

with open('24.txt', 'r', encoding='utf-8') as f:
    s = f.readline()
    counter = 0
    maxi = 0
    len_s = 0
    while len_s < len(s) - 1:
        if s[len_s:len_s + 2] == 'PC':
            counter += 2
            len_s += 2
        elif s[len_s:len_s + 4] == 'CSGO':
            counter += 4
            len_s += 4
        elif len_s > 0 and s[len_s - 1:len_s + 3] == 'CSGO':
            counter = 4
            len_s += 3
        else:
            counter = 0
            len_s += 1
        maxi = max(maxi, counter)
    print(maxi)

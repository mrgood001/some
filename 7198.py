with open('24.txt', 'r', encoding='utf-8') as f:
    s = f.readline()
    counter = 0
    maxi = 0
    ps = {'AB', 'CB', 'BC', 'BA'}
    for i in range(len(s)):
        if s[i:i+2] in ps:
            counter += 1
        else: counter = 0
        maxi = max(maxi, counter)
    print(maxi)

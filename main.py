with open('24.txt', 'r', encoding='utf-8') as f:
    s = f.readline()
    len_message = 0
    len_xyz = 0
    current_xyz = 0
    maxi = 0
    for i in s:
        if (i == 'X' and len_xyz % 3 == 0) or (i == 'Y' and len_xyz % 3 == 1) or (i == 'Z' and len_xyz % 3 == 2):
            len_xyz += 1
            current_xyz += 1
            if current_xyz > 2:
                maxi = max(maxi, len_message - 2)
                len_message = 0
            else:
                len_message += 1
        else:
            len_message += 1
            if current_xyz < 3:
                len_xyz -= current_xyz
            current_xyz = 0
    print(maxi)

from ipaddress import *
#1
# в net первое значение это ip адрес, второе значение из цикла это макси, ноль в net просто нужно ставить
for mask in range(33):
    net = ip_network(f'93.138.70.47/{mask}', 0)
    print(net)

#2 найти количество ip адресов с четным количеством 1
# первое значение в s это ip сети, второе это маска сети
counter = 0
net = ip_network('192.168.32.160/255.255.255.240')
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 2 == 0:
        counter +=1
print(counter)

#3 найти количество ip адресов с равным количеством 1 и 0
# первое значение в s это ip сети, второе это маска сети  
counter = 0
net = ip_network('192.168.248.176/255.255.255.240')
for ip in net:
    s = f'{ip:b}'
    if s.count('1') == s.count('0'):
        counter += 1
print(counter)

#4 найти количество ip адресов с большим количеством 1 чем 0
counter = 0
net = ip_network('192.168.248.176/255.255.255.240')
for ip in net:
    s = f'{ip:b}'
    if s.count('1') > s.count('0'):
        counter += 1
print(counter)



"""
def max_consecutive_vowels(s):
    vowels = set(['A', 'E', 'I', 'O', 'U', 'Y'])
    n = len(s)
    max_len = 0
    cur_len = 0
    cur_vowels = {}
    
    for i in range(n):
        if s[i] in vowels:
            if s[i] not in cur_vowels:
                cur_vowels[s[i]] = 1
            else:
                cur_vowels[s[i]] += 1
            
            if cur_vowels[s[i]] <= 8:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 0
                cur_vowels = {}
        else:
            cur_len += 1
            max_len = max(max_len, cur_len)
    
    return max_len

# Пример использования
text = "ABCDAAEEIIUUUOYYYBCDEFGHIJK"
print(max_consecutive_vowels(text))  # Выводит 13
"""

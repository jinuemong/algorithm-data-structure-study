
# 둘만의 암호
# 잘못된 문제 풀이 -> 다시 시도

def solution(s, skip, index):

    data_set = {}
    current ,skip_n= ord('a') , 0
    while current <= ord('z'):
        if chr(current) in skip:
            skip_n += 1

        if current+skip_n+index >ord('z'):
            data_set[chr(current)] = ord('a')
        else:
            data_set[chr(current)] = current+skip_n+index
        current+=1
    data_list = []
    for i in range(len(s)):
        data_list.append(chr(data_set[s[i]]))
    print(data_set,skip_n)
    return ''.join(data_list)

print(solution("aukks","wbqd",5))
print(chr(102))
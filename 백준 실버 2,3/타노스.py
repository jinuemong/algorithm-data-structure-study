# 0은 뒤에서
# 1은 앞에서 제거

st = list(input())
zero_size = st.count('0') // 2
one_size = (len(st) - zero_size*2)//2
for i in range(len(st) - 1, - 1, -1):
    if st[i] == '0':
        st[i] = -1
        zero_size-=1
        if zero_size == 0:
            break
for i in range(len(st)):
    if st[i] == '1':
        st[i] = -1
        one_size-=1
        if one_size == 0:
            break
print(''.join([i for i in st if i != -1]))
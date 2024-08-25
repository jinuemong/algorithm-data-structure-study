
# n = int(input())
# n_st = "IO"*n + "I"
# len_n = len(n_st)
# m = int(input())
# s = input().strip()
#
# count = 0
# for i in range(m - len_n+1):
#     if s[i:i+len_n] == n_st:
#         count+=1
# print(count)

n = int(input())
# n이 1씩 증가하면 IOI + 2
# 즉 n의 개수가 이동할 인덱스
n_st = "IO"*n + "I"
m = int(input())
s = input().strip()
i = 0
count = 0
while i < len(s)-len(n_st)+1:
    c = s[i:i+3]
    if c == "IOI":
        i+=2
        count+=1
    else:
        i+=1
print(count)
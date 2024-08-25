
# LCS 2
#
# # 공통 수열 찾ㄱ ㅣ
# # 2차원 배열 ?
# #    A C A Y K P
# # C  0 1 0 0 0 0
# # A  1 1 1 0 0 0
# # P  1 1 1 0 0 1
# # C  1 2 1 0 0 0
# # A  2 2 2 0 0 0
# # K  2 2 2 0 1 1
#
# a = input()
# b = input()
#
# max_s, min_s = "" , ""
# # 더 큰 수가 y
# if len(a) > len(b):
#     max_s = a
#     min_s = b
# else:
#     max_s = b
#     min_s = a
# data = [[False]*(len(min_s)) for i in range(len(max_s))]
# for y in range(len(max_s)):
#     for x in range(len(min_s)):
#         if y>=x and (max_s[y] == min_s[x]) or (y>0 and data[y-1][x]):
#             data[y][x] = True
# s_len = data[-1].count(True)
# print(s_len)
# if s_len>0:
#     for i,t in enumerate(data[-1]):
#         if t: print(min_s[i],end="")
#
# #    A C A Y K P
# # C  0 1 0 0 0 0
# # A  1 0 0 0 0 0
# # P  0 0 0 0 0 0
# # C  0 0 0 0 0 0
# # A  1 0 0 0 0 0
# # K  0 0 0 0 0 0

a = [0]+list(input())
b = [0]+list(input())

lcs = [[""]*len(a) for i in range(len(b))]
for i in range(1,len(b)):
    for j in range(1,len(a)):
        if a[j] == b[i]:
            lcs[i][j] = lcs[i-1][j-1] + a[j]
        else:
            if len(lcs[i][j-1]) > len(lcs[i-1][j]):
                lcs[i][j] = lcs[i][j-1]
            else:
                lcs[i][j] = lcs[i-1][j]
result = lcs[-1][-1]
print(len(result))
if len(result)>0:
    print(result)
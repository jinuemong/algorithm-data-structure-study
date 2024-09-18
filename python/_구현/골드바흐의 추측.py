stack = [int(input())]
max_value = 0
while True:
    new = int(input())
    if new == 0:
        break
    stack.append(new)
    max_value = max(new, max_value)
s = [1] * (max_value + 1)
for i in range(2, len(s)):
    if s[i]:
        for j in range(i * 2, len(s), i):
            s[j] = 0
for n in stack:
    flag = True
    for i in range(3,n+1,2):
        if s[i] and s[n-i]:
            print(n,"=",i,"+",n-i)
            flag = False
            break
    if flag:
        print("Goldbach's conjecture is wrong.")


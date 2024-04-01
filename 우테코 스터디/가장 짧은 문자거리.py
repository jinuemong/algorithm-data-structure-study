
s,t = input().split()
print(s,t)
t_list = []
for s_i in s:
    if s_i == t:
        t_list.append(0)
    else:
        t_list.append(101)

for t_i in range(len(t_list)):
    if t_list[t_i] == 1:
        min(s[t_i:].index(t),s[::t_i-1].index(t))

print(t_list)
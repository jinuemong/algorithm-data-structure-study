
s = input().split(" ")

s_list = dict()
for s_i in s:
    if s_i != "":
        s_i_low = s_i.lower()
        if s_i_low in s_list:
            s_list[s_i_low] +=1
        else:
            s_list[s_i_low] = 1

print(sum(s_list.values()))

s = list(input())
s_list = []
prev_op = 1
prev_st = ""
for i in s:
    if i == "-" or i == "+":
        s_list.append(prev_op * int(prev_st))
        prev_st = ""
        prev_op = int(i + "1")
    else:
        prev_st+=i
s_list.append(prev_op * int(prev_st))
result = []
def find(current,next):
    if len(next) == 0:
        result.append(current)
    for i in range(1,len(next)+1):
        print(next[:i],next[i:])
        find(current+sum(next[:i]),next[i:])
find(0,s_list)
print(min(result))
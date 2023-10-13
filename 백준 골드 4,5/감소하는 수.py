


# 골드 5

n = int(input())

result = []

def make_number(data):
    result.append(int(data))
    for i in range(int(data[-1])):
        make_number(data+str(i))

for i in range(10):
    make_number(str(i))

if len(result)<=n:
    print(-1)
else:
    print(sorted(result)[n])
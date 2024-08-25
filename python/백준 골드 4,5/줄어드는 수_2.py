

# 50000번째 수 까지 탐색
# # 정렬 후 인덱스-1  출력


data_list = []
n = int(input())
def check(data):
    data_list.append(int(data))
    for i in range(int(data[-1])):
        next = data+str(i)
        check(next)
for i in range(10):
    check(str(i))
if n-1 <len(data_list):
    print(sorted(data_list)[n-1])
else:
    print(-1)

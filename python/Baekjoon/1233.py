# https://www.acmicpc.net/problem/1233

answer = dict()

s1,s2,s3 = list(map(int,input().split()))

for s_1 in range(1,s1+1):
    for s_2 in range(1,s2+1):
        for s_3 in range(1,s3+1):
            data = s_1+s_2+s_3
            if data in answer:
                answer[data]+=1
            else:
                answer[data]=0
max_key,max_value = 0 , 0
for key,value in answer.items():
    if value>max_value:
        max_key=key
        max_value=value
    elif value==max_value:
        if max_key>key:
            max_key=key
            max_value=value
print(max_key)

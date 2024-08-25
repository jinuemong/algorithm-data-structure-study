

# 남학생 : 번호가 받은 수의 배수이면 스위치의 상태를 바꿈 1-> 0  or 0 -> 1
# 여학생 : 자신이 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우 대칭만큼 상태를 바꿈
# ex > 3선택 -> 2,4 대칭 확인 -> 1,5 대칭 확인 1~5 전환

n =  int(input())
switch = list(map(int,input().split()))

def man(num):
    for idx in range(num,len(switch)+1,num):
        if switch[idx-1] == 1:
            switch[idx-1] = 0
        else :
            switch[idx-1] = 1
def woman(num):
    i = 0
    while 0<=num-i-1 and num+i+1 <len(switch):
        if switch[num-i-1] != switch[num+i+1]:
            break
        i+=1
    for j in range(num-i,num+i+1):
        if switch[j] == 1:
            switch[j] = 0
        else:
            switch[j] = 1

for _ in range(int(input())):
    sex, number = list(map(int,input().split()))
    if sex == 1:
        man(number)
    else:
        woman(number-1)

for idx,s in enumerate(switch):
    print(s, end=" ")
    if (idx+1)%20 == 0:
        print()


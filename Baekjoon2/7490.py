
# [ 문제 이해 ]

# 1부터 N까지의 수를 오름차순으로 쓴 수열 1,2,3,,,N
# + , - , 공백을 사이에 삽입
# + : 더하기 , - : 빼기 , 공백 : 수 합치기
# N이 주어졌을 때 수식의 결과가 0이 되는 모든 수식을 찾음

# 테스트 케이스 수, 자연수 N

# ex > n = 3인 경우 -> 1+2-3 (1가지 수) + print()
# eX > n = 7인 경우 -> 1+2-3+4-5-6+7....

# 아스키 순서에 따라서 출력해야 하므로 + - 공백 순

# 자연수 N의 범위가 한정적이므로 완전 탐색 알고리즘 사용
# -> 수 리스트와 연산자 리스트 분리해서 경우의 수 계산

# N이 2인 경우 [공백,-,+] 는 3의 1 제곱의 경우의 수만 존재
# 1,2 -> 1과 2 사이에 3가지 경우의 수
# N이 3인 경우 [공백,-,+] 는 3의 2 제곱의 경우의 수만 존재
# 1,2,3 -> 1과 2와 3 사이에 3*3가지의 경우의 수

#즉 3의 N 제곱의 경우의 수 중에서 0이 되는 값이 있을 경우만 출력

# i : 다음 수 , num : 다음에 연산 할 값
def operation(i,op,num,result,op_string):
    global n
    if op==' ':
        num+=str(i)
        op_string+= (" "+str(i))
    elif op =='+':
        result+=int(num)
        op_string += ('+'+str(i))
    elif op =='-':
        result-=int(num)
        op_string += ('-' + str(i))

    if i == n: # 마지막 연산
        if result==0:
            print(op_string)
            return

    if op!=' ':
        #다음 연산 진행
        num=i+1
    operation(i+1, ' ', num,result,op_string)
    operation(i+1, '+', num,result,op_string)
    operation(i+1, '-', num,result,op_string)



for _ in range(int(input())):
    n = int(input())
    operation(1,' ',"1", 0,"")
    operation(1,'+',"1", 0,"")
    operation(1,'-',"1", 0,"")


# "" 만날 경우 부호를 붙인 후에 다음 연산에 따라서 수행
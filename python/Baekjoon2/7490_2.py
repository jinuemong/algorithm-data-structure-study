

# eval() 함수로 문자열 형태의 표현식 계산

import copy

# array : 호출 시 마다 매개변수로 들어가서 함수로 호출 (경우당 3번)
# n의 길이를 가지면 멈추기
# 깊은 복사를 통해서 동일한 array를 공유하지 않도록 함

# recursive : op 리스트를 제작하는 함수
def recursive(array,n):
    if len(array)==n:
        op_list.append(copy.deepcopy(array))
        return
    array.append(' ')
    recursive(array,n)
    array.pop()

    array.append('+')
    recursive(array,n)
    array.pop()

    array.append('-')
    recursive(array,n)
    array.pop()

t = int(input())

for _ in range(t):
    # 매 케이스마다 새로운 연산 리스트 생성
    op_list = []
    n = int(input())
    recursive([],n-1) #n-1의 3의 제곱만큼 제작 op 리스트

    integers = [i for i in range(1,n+1)]

    # 연속된 수 사이에 연산자 리스트 내용을
    # 순서대로 하나씩 넣어서 string 제작
    for op in op_list:
        string = ""
        for i in range(n-1):
            string += str(integers[i]) + op[i]
        string += str(integers[-1])
        # eval 함수를 통해서 연산 진행
        # 공백으로 된 부분을 지움
        if eval(string.replace(" ","")) == 0:
            print(string)
    print()
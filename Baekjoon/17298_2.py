# 출처 : https://www.acmicpc.net/problem/17298
# 포스팅
import sys

n = int(sys.stdin.readline().strip())
n_list = list(map(int,sys.stdin.readline().strip().split()))

stack = []
answer = [-1]*n
for i in range(n):
    item = n_list[i]

    # 스택에 아무것도 없거나 마지막 값보다 작거나 같은 경우 push
    if len(stack)==0 or stack[-1][0] >=item:
        stack.append((item,i))
    else:
        while len(stack)>0:
            #스택을 뒤에서부터 확인
            prev_item, index = stack[-1]

            if prev_item<item:
                stack.pop()
                answer[index] = item
            else:
                break
        stack.append((item,i)) #현재 값 push

for a in answer:
    print(a,end=" ")




# 영재의 택배 상자
# 1~ n 일렬
# 벨트에 놓인 순서대로만 상자를 내릴 수 있음
# 보조 컨테이너 활용
# 앞 뒤로 이동 가능, 맨 앞의 상자만 뺄 수 있음
# 가장 마지막에 보관된 상자 빼기 가능 (스택
# 보조까지 이용해서 원하는 순새대로 하지 못한다면 실패

# 1. main에서 하나씩 꺼냄 (main은 1부터 n까지 순서대로)
# 2. order[0]와 같은지 확인
# 3. 만약 order[0] 과 같다면 매칭
# 4. 아니라면 sub[-1]과 비교 (while -> 서브는 계속 탐색 )
# 5. 둘 다 아니라면 main에서 하나 더 꺼냄
# 6. 만약 메인에서 다꺼내고, sub[-1]과 매칭이 안된다면, 종료

from collections import  deque
def solution(order):
    main,sub = deque([i for i in range(1,len(order)+1)]),[]
    order , answer = deque(order),0
    while main:
        sub.append(main.popleft())
        if order[0]== sub[-1]:
            while sub and order:
                if sub[-1] == order[0]:
                    answer+=1
                    order.popleft(),sub.pop()
                else:
                    break

    return answer


# order = [5, 4, 3, 2, 1]
order = [4, 3, 1, 2, 5]
print(solution(order))

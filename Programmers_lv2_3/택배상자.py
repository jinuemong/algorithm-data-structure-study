


# 영재의 택배 상자
# 1~ n 일렬
# 벨트에 놓인 순서대로만 상자를 내릴 수 있음
# 보조 컨테이너 활용
# 앞 뒤로 이동 가능, 맨 앞의 상자만 뺄 수 있음
# 가장 마지막에 보관된 상자 빼기 가능 (스택
# 보조까지 이용해서 원하는 순새대로 하지 못한다면 실패

# 즉 본 벨트(큐), 보조 벨트(스택)
# 모두를 사용해서 원하는 대로 꺼낼 수 없다면
# 꺼낸 수만큼만 출력
# 본 컨테이너 : 1번 상자 부터 내릴 수 있음
# 1 2 3 4 5
# 맨 앞 pop
# 보조 컨테이너 : 마지막 상자 부터 내릴 수 있음
# 1 2 3 4 5
# 맨 뒤 pop
# sub : 1, 2, 3
# 5 4 /3 /2 /1
# 5 2 1 3 4
from collections import deque
def solution(order):
    main_contain, sub_contain = deque([i for i in range(1,len(order)+1)]),[]
    order ,answer =  deque(order),0
    while order:
        data = order.popleft()

            




    return answer

order = [5, 4, 3, 2, 1]
order = [4, 3, 1, 2, 5]
print(solution(order))

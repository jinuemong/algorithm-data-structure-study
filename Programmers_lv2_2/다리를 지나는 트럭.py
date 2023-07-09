
# 다리를 지나는 트럭
# 최대 무게를 넘지 않는 다리를 트럭들이 지나는 시간,
# 트럭은 1초에 1개의 다리 길이를 건널 수 있음
# deque를 통해서 다리를 건너는 과정 : 0으로 deque 초기화 (다리 길이 만큼)
# 새로운 트럭이 들어갈 수 있는 경우 : 남은 무게보다 현재 트럭의 무게가 작거나 같은 경우
# 트럭이 들어갈 수 없는 경우: 왼쪽에 0 삽입
# 트럭이 나오는 경우 : 남은 무게에 + 트럭 무게 , 나온 트럭의 수 count
# 0이 나오는 경우 : 남은 무게에 +0, 나온 트럭 수 x
# 매 과정에 초 카운트 +1
# 나온 트럭 수 = 총 트럭 수 인 경우 종료

from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue,count = deque([0 for _ in range(bridge_length)]),len(truck_weights)
    while count>0: # 남은 트럭이 없을 때까지
        answer+=1
        out_truck = queue.pop()
        weight+=out_truck # out truck or 0
        if out_truck>0:
            count-=1
        if len(truck_weights)>0 and truck_weights[-1] <= weight: #새로운 트럭 들어감
            in_truck =truck_weights.pop()
            queue.appendleft(in_truck)
            weight-=in_truck
        else:
            queue.appendleft(0)
    return answer

print(solution(100,100 ,[10]))

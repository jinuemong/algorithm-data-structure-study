
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

print()
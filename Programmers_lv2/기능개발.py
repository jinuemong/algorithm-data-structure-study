import heapq ,math
# 기능개발
# 각 기능의 진행률, 스피드로 종료 시간 계산
# 앞이 배포되는 기간 동안 먼저 개발이 끝난 것은 배포를 기다려야 함

def solution(progresses, speeds):
    answer = []
    heap = []
    for progress, speed in zip(progresses,speeds):
        data =math.ceil((100-progress)/speed) # 나머지가 있을 경우 올림

        if len(heap)!=0:
            if heap[0][1] <= data:
                answer.append(len(heap))
                print("kep", heap[0][1])
                heap = []
            else:
                heapq.heappush(heap,(-data,data))
        else:
            heapq.heappush(heap, (-data, data))
            print("paa")
        print(data,heap)


    return answer

progresses =[93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses,speeds))
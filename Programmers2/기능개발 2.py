
# 기능개발
# 각 기능의 진행률, 스피드로 종료 시간 계산
# 앞이 배포되는 기간 동안 먼저 개발이 끝난 것은 배포를 기다려야 함
# ceil 함수를 통해서 나머지가 있을 경우 올림
def solution(progresses, speeds):
    import math
    answer = [1]
    data_list = [math.ceil((100-progress)/speed) for progress, speed in zip(progresses, speeds)]

    prev= data_list[0]
    for i in range(1,len(data_list)):
        if prev >= data_list[i]:
            answer[-1]+=1
        else:
            prev = data_list[i]
            answer.append(1)
    return answer

progresses =[95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses,speeds))
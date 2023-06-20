
# 피로도
# 최소 피로도 : 해당 던전을 탐험하기 위해 가지고 있어야할 피로도
# 소모 피로도 : 던전 탐험 후의 소모 피로도
# 최대한 많은 던전 탐험 : 최소 피로도와 소모 피로도를 계산해서 최적해 탐색

answer = 0
def solution(k, dungeons):
    # set 사용을 위해서 i로 구분
    global answer
    idx = set([i for i in range(len(dungeons))])
    find(k,dungeons,set(),idx,0)
    return answer

def find(k,dungeons,visited,idx_list,cnt):
    global answer
    if cnt > answer:
        answer = cnt
    for i in idx_list:
        if i not in visited and k- dungeons[i][0] >=0:
            visited.add(i)
            find(k-dungeons[i][1],dungeons,visited,idx_list-set([i]),cnt+1)
            visited.remove(i)
k = 80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k,dungeons))
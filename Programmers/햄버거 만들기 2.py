
# 햄버거 만들기
# 1: 빵, 2 : 야채 3 : 고기
# 빵 - 야채 - 고기 -빵  (1231) -> 햄버거 하나
# 무조건 순서대로 쌓아야 함
# 1->2  2-> 3  3 -> 4 순으로 업그레이드
# i 가 1인 경우 -> 3번이 0이 아니라면 4번 추가, 3번 감소
# 그 외의 경우는 1 넣을 시
def solution(ingredient):
    data_set  = {0:1000000,1:0, 2:0,3:0,4:0} # 0 : 쓰레기 값
    for i in ingredient:
        if i==1 and data_set[3]>0: # 햄버거 완성
            data_set[3]-=1
            data_set[4]+=1
        elif data_set[i-1]>0: # 햄버거 쌓기
            data_set[i-1]-=1
            data_set[i]+=1
        print(i,data_set)
    return data_set[4]



ingredient =[2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))
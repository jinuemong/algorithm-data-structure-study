

# 키패드 누르기

left_list  = {1,4,7}
right_list = {3,6,9}
# mid_list = {2,5,8,0}  더 가까운 것 사용
data_set = {
    1 : [1,1], 2: [1,2],3:[1,3]
    ,4:[2,1],5:[2,2],6:[2,3]
    ,7:[3,1],8:[3,2],9:[3,3],0:[4,2]}
def solution(numbers,hand):
    answer = ''
    #  0 : 1,2,3 , 1: 4,5,6 , 2: 7,8,9 , 3 : *,0,#
    hand = {"L" : [4,1],"R" : [4,3],"hand" : hand[0].upper()}
    print(hand)
    for n in numbers:
        now = data_set[n]
        print(hand['L'],hand['R'],end=' ')
        if n in left_list: # 왼쪽 클릭
            hand['L'] = now
            answer += 'L'

        elif n in right_list: #오른쪽 클릭
            hand['R'] =  now
            answer += 'R'

        else: # 중앙 클릭

            if find_d(now,hand['L']) < find_d(now,hand['R']): #왼
                hand['L'] =  now
                answer+='L'
            elif find_d(now,hand['L']) > find_d(now,hand['R']): # 오
                hand['R'] = now
                answer+='R'
            else: #주 손 사용
                hand[hand["hand"]] = now
                answer+=hand["hand"]
        print(n,answer[-1])
    return answer

def find_d(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

print(solution(numbers,hand))
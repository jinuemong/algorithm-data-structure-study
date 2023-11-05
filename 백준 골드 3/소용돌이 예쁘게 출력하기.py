
r1,c1,r2,c2 = list(map(int,input().split()))
# r1,c1을 기준으로 r2,c2를 포함하는 정사각형 생성해서 좌표 이동
current,current_num = (abs(r1),abs(c1)), "1"
r2-=r1
c2-=c1
r1 = 0
c1 = 0
direction = [(0,1),(-1,0),(0,-1),(1,0)]

print(current)
rec_len = max(current[0],current[1])
data_list = [["0"]*(rec_len*2+1) for i in range(rec_len*2+1)]
data_list[current[0]][current[1]]= current_num
rotation ,total= 0, rec_len**2
while total>int(current_num):
    print(data_list)
    next = direction[rotation%4]
    next_next = direction[(rotation+1)%4]
    current = (current[0]+next[0],current[1]+next[0])
    current_num = str(int(current_num)+1)
    data_list[current[0]][current[1]] = current_num


    print(data_list)


len_num = len(current_num)
for i in range(r1,r2+1):
    for j in range(c1,c2+1):
        print((len_num-len(data_list[i][j]))*" "+data_list[i][j],end=" ")
    print()

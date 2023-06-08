
# 프로그래머스 : 바탕화면 정리

# [방법]
# 제일 작은 x좌표를 찾음
# 제일 작은  y좌표를 찾음
# 두 좌표가 같을 경우 해당 지점 부터 드래그
# 두 좌표가 다를 경우 두 좌표의 직선이 만나는 점 탐색
# -> rdx,rdy

# 제일 큰 x좌표를 찾음
# 제일 큰 y좌표를 찾음
# 두 좌표가 같을 경우 해당 지점 까지 드래그
# 두 좌표가 다를 경우 두 좌표의 직선이 만나는 점 탐색
# -> lux,luy

def solution(wallpaper):
    answer = []
    min_x,min_y = 50,50
    max_x,max_y = 0,0

    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[0])):
            data = wallpaper[y][x]
            if data == "#":
                if y < min_y:
                    min_y = y
                if y > max_y:
                    max_y = y
                if x < min_x:
                    min_x = x
                if x > max_x:
                    max_x = x
    answer = [min_y,min_x,max_y+1,max_x+1]
    return answer


wallpaper =["..........", ".....#....", "......##..", "...##.....", "....#....."]
print(solution(wallpaper))

# 1,5 (가장 작은 y)
# 3,3 (가장 작은 x)
# -> 1,3 (가장 작은 y , 가장 작은 x)

# 4,4 (가장 큰 y)
# 2,7 (가장 큰 x)
# -> 4,7 (가장 큰 y, 가장 큰 x )

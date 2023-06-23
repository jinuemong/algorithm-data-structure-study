

# 방문 기록
# start : 4,4

def solution(dirs):
    data_set,i,j =set(),5,5
    for dir in list(dirs):
        if dir=="U" and 0<=j-1:
            data_set.add(((j, i), (j-1, i)))
            j-=1
        elif dir == "D" and j+1<=10:
            data_set.add(((j, i), (j+1, i)))
            j+=1
        elif dir == "R" and i+1<=10:
            data_set.add(((j, i), (j, i+1)))
            i += 1
        elif dir == "L" and 0<=i-1:
            data_set.add(((j,i),(j,i-1)))
            i -= 1
    return len(data_set)

dirs = "ULURRDLLU"
print(solution(dirs))
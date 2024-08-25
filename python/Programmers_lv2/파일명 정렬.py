


# 파일명 정렬

# 기본적으로 숫자 숫으로 오름차순 정렬
# 9 - 10 - 0011 - 012 - 13 - 014 순
# head, number이 같을 경우 원래의 인덱스 순서를 유지한다 ! *

import re
def solution(files):
    answer = []
    for idx,file in enumerate(files):
        data = [ i.start() for i in re.finditer(f"[0-9]",file)]
        for i in range(1, len(data)):
            if data[i]!= data[i-1]+1:
                data = data[:i] #인덱스 컷
                break
        num = int("".join([file[i] for i in data]))
        head = file[:data[0]].upper()
        answer.append([head,num,idx,file])
    return [ data[3] for data in sorted(answer)]

print(solution( ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
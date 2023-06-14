

def solution(strings, n):
    return [i[1] for i in sorted([[string[n],string] for string in strings])]

strings = ["sun", "bed", "car"]
n = 1

print(solution(strings,n))
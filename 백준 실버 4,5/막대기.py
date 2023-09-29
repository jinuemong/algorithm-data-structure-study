

# 막대기

def solve():
    x = int(input())
    result = 0
    while x>0:
        if x%2==1:
            result+=1
        x=x//2
    return result
print(solve())
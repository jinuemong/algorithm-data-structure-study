
n = int(input())

stack = [(0,100_000_000)]
tops = list(map(int,input().split()))
result = []
for i,top in enumerate(tops):
    while stack:
        if stack[-1][1] >= top:
           result.append(stack[-1][0])
           stack.append((i+1,top))
           break
        else:
            stack.pop()
for r in result:
    print(r,end=" ")
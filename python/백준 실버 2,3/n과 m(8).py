
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
n_list = sorted(set(list(map(int,input().split()))))

answer = []

def back(depth,idx):
    if depth == m:
        print(' '.join(map(str,answer)))
        return

    for i in range(idx,len(n_list)):
        answer.append(n_list[i])
        back(depth+1,i)
        answer.pop()
back(0,0)

# 가희와 키워드
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

keyword_list = set([input().rstrip() for i in range(n)])
delete_list = set()
for i in range(m):
    blog = input().rstrip().split(",")
    for b in blog:
        if b in keyword_list and b not in delete_list:
            delete_list.add(b)
    print(len(keyword_list) - len(delete_list))
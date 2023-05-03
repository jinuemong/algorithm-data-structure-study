
# n이 최대 100

t = int(input())
book_dic = {}

# 책 이름 : count로 정렬
for _ in range(t):
 book = input()
 if book in book_dic:
  book_dic[book]+=1
 else:
  book_dic[book]=1

max_num,max_name = 0,""
for book, count in book_dic.items(): #아이템 확인
 if max_num<count: #더 높은 값 찾기
  max_name = book
  max_num=count
 elif max_num==count: # 값이 같을 경우 사전 순 낮은 값 찾기
  if max_name>book or max_name=="":
   max_name = book


print(max_name)


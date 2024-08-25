# https://www.acmicpc.net/problem/2696

import heapq

t = int(input())
max_heap = []  # 최대 힙 (중앙 값보다 작은 집합)
# 최대 힙은 (-n , n)으로 넣고 heappop(heap)[1]로 꺼냄

min_heap = []  # 최소 힙 (중앙 값보다 큰 집합)
answer = []


def setQ(index,n_1, n_2):
    heapq.heappush(min_heap, max(n_1, n_2))
    min_n = min(n_1, n_2)
    if index % 2 == 0:
        answer.append(min_n)
    heapq.heappush(max_heap, (-min_n, min_n))


for _ in range(t):

    m = int(input())
    len_m = int(m / 10) + 1
    m_list = []
    for i in range(len_m):
        m_list.append(list(map(int, input().split())))

    for j in range(len_m):
        for i in range(0, len(m_list[j])):

            new_data = m_list[j][i]
            if len(max_heap) == 0 and len(min_heap) == 0:
                # 첫 번째 값을 넣어줌
                heapq.heappush(min_heap, new_data)
                answer.append(new_data)
            elif len(max_heap) > len(min_heap):
                n = heapq.heappop(max_heap)[1]
                setQ(i,n,new_data)

            elif len(max_heap) < len(min_heap):
                n = heapq.heappop(min_heap)
                setQ(i,n,new_data)

            elif len(max_heap) == len(min_heap):
                n_1 = heapq.heappop(max_heap)[1]
                n_2 = heapq.heappop(min_heap)

                if new_data < n_1:  # new data 최소, n_1 중앙, n_2 최대
                    heapq.heappush(min_heap, n_2)  # 최대
                    heapq.heappush(min_heap, n_1)  # 중앙
                    if i % 2 == 0:
                        answer.append(n_1)
                    heapq.heappush(max_heap, (-new_data, new_data))

                elif n_2 < new_data:  # new_data 최대, n_1최소, n_2 중앙
                    heapq.heappush(min_heap, new_data)  # 최대
                    heapq.heappush(min_heap, n_2)  # 중앙
                    if i % 2 == 0:
                        answer.append(n_2)
                    heapq.heappush(max_heap, (-n_1, n_1))
                else:  # new_data 중앙 n_1최소 n_2 최대
                    heapq.heappush(min_heap, n_2)  # 최대
                    heapq.heappush(min_heap, new_data)  # 중앙
                    if i % 2 == 0:
                        answer.append(new_data)
                    heapq.heappush(max_heap, (-n_1, n_1))

    answer_count = 0
    print(len(answer))
    for i in range(len(answer)):
        print(answer[i], end=' ')
        answer_count += 1
        if answer_count == 10 or i==len(answer)-1:
            answer_count = 0
            print()

    max_heap = []
    min_heap = []
    answer = []

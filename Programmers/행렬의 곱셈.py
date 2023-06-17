

def solution(arr1, arr2):
    answer = []
    for arr_x in arr1:
        data_list = []
        for arr_y  in list(zip(*arr2)):
            data_list.append(sum([x*y for x,y in zip(arr_x,arr_y)]))
        answer.append(data_list)



    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1,arr2))
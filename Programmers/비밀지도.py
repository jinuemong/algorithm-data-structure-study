
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        answer.append((''.join(data_ex(n,i,j))))
    return answer

def data_ex(n,x,y):
    result,i = [' ' for _ in range(n)],n-1
    while i>=0:
        if x%2==0 and y%2==0:
            result[i] = " "
        else:
            result[i] = "#"
        x, y = (x // 2), (y // 2)
        i-=1
    return result

n = 6
arr1	=	[46, 33, 33 ,22, 31, 50]
arr2	=	[27 ,56, 19, 14, 14, 10]
print(solution(n,arr1,arr2))
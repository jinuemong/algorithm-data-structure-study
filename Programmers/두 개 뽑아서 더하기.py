
def solution(numbers):
    data_set = set()
    for i in range(0,len(numbers)):
        for j in range(i+1, len(numbers)):
            data_set.add(numbers[i]+numbers[j])
    return sorted(list(data_set))



numbers = [2,1,3,4,1]
print(solution(numbers))

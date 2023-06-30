

# 두 개 이하로 다른 비트

# f(x) : x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수
# 경우의 수가 많으므로 최적의 알고리즘을 구해야 함
# xor 연산을 통해서 서로 다른 수를 찾을 수 있다
# -> 값이 다를 경우 트루
# 연산 후 해당 값의 합이 2보다 작거나 같아야 함
def solution(numbers):
    answer = []
    for number in numbers:
        i = number
        while True:
            i+=1
            data = check_xor(make_bit(number),i)
            if data!=-1:
                answer.append(data)
                break
    return answer
def check_xor(number_bit,data):
    data_bit,count= make_bit(data),0
    max_len = max(len(number_bit),len(data_bit))
    number_bit = (max_len-len(number_bit))*"0"+number_bit
    data_bit = (max_len-len(data_bit))*"0"+data_bit
    for i,j in zip(number_bit,data_bit):
        if i!=j:
            count+=1
    if count<=2:
        return data
    else:
        return -1
def make_bit(data):
    result = ""
    while data>0:
        result = str(data%2)+result
        data//=2
    return result

print(solution([i for i in range(10000,100000)]))
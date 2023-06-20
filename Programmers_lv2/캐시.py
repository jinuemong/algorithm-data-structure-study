


# 캐시
def solution(cacheSize, cities):
    answer = 0
    data_set =  {}
    for i , city in enumerate(cities):
        city = str(city).lower()
        if city in data_set:
            answer+=1 # cash hit
            data_set[city] = i
        else:
            answer+=5 # cash miss
            data_set[city] = i
            if len(data_set)>cacheSize:
                min_key,min_data = 0,100001
                for key,value in data_set.items():
                    if value<min_data:
                        min_key,min_data = key,value
                data_set.pop(min_key)
    return answer

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize,cities))
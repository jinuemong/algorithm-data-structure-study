

# 주차 요금 계산
import re ,math
def solution(fees, records):
    last_in_data , total_count = {}, {}
    for record in records:
        hour,minute, car, type = re.split('[: ]',record)
        if type == "OUT":
            # car[0] : 시간, car[1] : 분
            time = (int(hour)-int(last_in_data[car][0]))*60 + (int(minute)-int(last_in_data[car][1]))
            if car in total_count:
                 total_count[car]+=time
            else:
                total_count[car] = time
            last_in_data.pop(car)
        else:
            last_in_data[car] = [hour,minute]
    for key, data in last_in_data.items():
        if key in total_count:
            total_count[key]+= ((23 - int(data[0]) )* 60 + (59 - int(data[1])))
        else:
            total_count[key] = ((23 - int(data[0])) * 60 + (59 - int(data[1])))
    return [fees[1]+(math.ceil( (value-fees[0])/fees[2]))*fees[3] if value > fees[0] else fees[1]
     for car,value in sorted(total_count.items()) ]


     # 기본시간 기본 요금 단위 시간 단위 요금
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN",
           "06:34 0000 OUT", "07:59 5961 OUT",
           "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN",
           "23:00 5961 OUT"]
print(solution(fees,records))


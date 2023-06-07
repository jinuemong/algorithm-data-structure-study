def solution(name, yearning, photo):
    answer = [0]*len(photo)
    data_list = {}
    for i in range(len(name)):
        data_list[name[i]] = yearning[i]

    for j in range(len(photo)):
        for image in photo[j]:
            if image in data_list:
                answer[j]+=data_list[image]

    return answer


name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
print(solution(name,yearning,photo))
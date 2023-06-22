def solution(record):
    data_set_name =  {} # 아이디 : 닉네임
    answer = []
    # 세트에 추가한 후 answer에 등록 된 아이디 별 닉네임으로 전환
    for reco in record:
        reco_data = reco.split(" ")
        if reco_data[0] == "Enter":
            answer.append(reco_data[1]+"님이 들어왔습니다.")
        elif reco_data[0] == "Leave":
            answer.append(reco_data[1] + "님이 나갔습니다.")
        if len(reco_data)>2:
            data_set_name[reco_data[1]] = reco_data[2]
    for idx,a in enumerate(answer):
        answer[idx] = a.replace(a[0:a.index("님")],data_set_name[a[0:a.index("님")]])
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
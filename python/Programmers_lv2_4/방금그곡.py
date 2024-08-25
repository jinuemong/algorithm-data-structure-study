

# 카카오 블라인드
# C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개
# 1분에 1개 재생
# 처음부터 재생, 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복 재생
# 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생
# 음악이 00:00을 넘겨서 재생되는 경우는 없음
# 조건 음악이 여러개일 경우, 라디오에서 재생 된 시간이 제일 긴 음악 제목을 반환
# 재생 된 시간이 같을 경우는 먼저 입력된 음악 제목 반환
# 조건이 일치하는 음악이 없다면 (None) 반환

# 멜로디를 담은 문자열 m
# 방쇵된 곡의 정보를 담고있는 배열 musicinfos
# musicinfo : 시작 시간, 끝난 시간, 음악 제목, 악보 제목

def solution(m, musicinfos):
    # answer 0 : 크기, answer 1 : 인덱스
    answer = []

    for idx, musicinfo in enumerate(musicinfos):
        start, end, name, play = musicinfo.split(",")
        play_time = int(end.split(":")[0])*60 + int(end.split(":")[1]) - int(start.split(":")[0])*60 - int(start.split(":")[1])
        play_list,i = '', 0
        while i<play_time:
            if i+ len(play) > play_time:
                play_list+=play[i:play_time-i]
                i+= play_time-i
            else:
                play_list+=play
                i += len(play)
        if m in play_list:
            answer.append([play_time,idx,name])
    if len(answer)>0:
        return sorted(answer,key = lambda answer:(-answer[0],answer[1]))[0][2]
    else:
        return "(None)"

print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))

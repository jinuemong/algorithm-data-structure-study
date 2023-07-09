

# 영어 끝말 잇기
# 1부터 n까지 번호가 붙어있는 n명의 사람이 끝말잇기
# 1-> 2 -> ,,,, -> n -> 1 ->2...
# 앞 사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 함
# 이전에 등장한 단어는 사용 불가능
# 한 글자도 불가능
# 가장 먼저 탈락한 번호와 그 사람이 몇 번째 차례에서 탈락하는지 구하라
def solution(n, words):
    n_list,n_set= [i%n+1 for i in range(len(words))], set([words[0]])
    for i in range(1,len(words)):
        if words[i][0]!=words[i-1][-1] or words[i] in n_set:
            return [n_list[i],i//n+1]
        n_set.add(words[i])
    return [0,0]
print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
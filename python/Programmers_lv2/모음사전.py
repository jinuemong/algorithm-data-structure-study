

# 모음 사전

from itertools import product
def solution(word):
    return sorted(["".join(list(data)) for i in range(1,6) for data in product("AEIOU",repeat = i)]).index(word)+1

word = "AAAAE"

print(solution(word))


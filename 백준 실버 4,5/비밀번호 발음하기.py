

# 3연속 모음 or 자음이 와서는 안됨
# 연속 두 글자가 같으면 안됨, ee, oo 는 허용

consonant = {"a","e","i","o","u"}

while True:
    word = input().strip()
    if word == "end":
        break
    con_count, possible = 0, True
    if not 1<=len(word)<=20 or not word.islower():
        possible = False
    else:
        for i, w in enumerate(word):
            if w in consonant:
                con_count += 1
            if i > 2:
                if w in consonant and word[i - 1] in consonant and word[i - 2] in consonant:
                    possible = False
                    break
                elif w not in consonant and word[i - 1] not in consonant and word[i - 2] not in consonant:
                    possible = False
                    break
            if i > 0 and w == word[i - 1]:
                if w not in {'e','o'}:
                    possible = False
                    break

    if possible and con_count> 0:
        print("<{0}> is acceptable.".format(word))
    else:
        print("<{0}> is not acceptable.".format(word))




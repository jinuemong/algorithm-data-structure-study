
def listToInt(st):
    result = ""
    for s in st:
        result+=s+""
    return int(result.strip())

n = int(input())
n_list = list(str(n))
print(listToInt(n_list))

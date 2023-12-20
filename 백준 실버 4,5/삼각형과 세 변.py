
def find(a ,b ,c):
    if max(a,b,c) * 2 - sum([a,b,c]) >= 0 :
        return "Invalid"
    if a== b == c:
        return "Equilateral"
    elif a == b != c or b == c != a or a == c !=b :
        return "Isosceles"
    elif a != b != c:
        return "Scalene"


while True:
    a, b, c = list(map(int, input().split()))
    if sum([a, b, c]) == 0:
        break
    print(find(a,b,c))

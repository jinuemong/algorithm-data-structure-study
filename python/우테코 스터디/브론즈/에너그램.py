# a 조합으로 b를 만들수 있는지


t = int(input())

for _ in range(t):
    a, b = input().split()
    if sorted(a) == sorted(b):
        print(a + " & " + b + " are anagrams.")
    else:
        print(a + " & " + b + " are NOT anagrams.")

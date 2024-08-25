n = int(input())
cards = list(map(int, input().split()))

result = [0 for i in range(n)]

if n >= 2: result[1] = bin(cards[0] ^ cards[1]).count("1")
if n >= 3: result[2] = bin(cards[0] ^ cards[1] ^ cards[2]).count("1")
if n >= 4: result[3] = bin(cards[2] ^ cards[3]).count("1") + result[1]

for i in range(4, n):
    xor_1 = bin(cards[i - 1] ^ cards[i]).count("1")
    xor_2 = bin(cards[i] ^ cards[i - 1] ^ cards[i - 2]).count("1")
    result[i] = max(result[i - 2] + xor_1, result[i - 3] + xor_2)

print(result[-1])

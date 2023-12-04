
games = {"Y" : 1, "F" : 2 , "O" : 3 }

n, game = list(input().split())

name_set = set([input() for i in range(int(n))])

print(len(name_set)//games[game])
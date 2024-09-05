
n = int(input())
graph = []
for _ in range(n):
    graph.append([int(x) for x in list(input())])

def quad_tree(n, current):
    s = 0
    for i in current:
        s += sum(i)
    if s == n ** 2:
        return '1'
    if s == 0:
        return '0'

    temp = '('
    temp += quad_tree(n // 2, [i[:n // 2] for i in current[:n // 2]])
    temp += quad_tree(n // 2, [i[n // 2:] for i in current[:n // 2]])
    temp += quad_tree(n // 2, [i[:n // 2] for i in current[n // 2:]])
    temp += quad_tree(n // 2, [i[n // 2:] for i in current[n // 2:]])
    temp += ')'
    return temp

print(quad_tree(n,graph))

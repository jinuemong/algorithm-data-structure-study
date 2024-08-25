
from itertools import permutations
data_set = ['a' ,'b' ,'c']
for i in permutations(data_set, 2):
    print("".join(i) ,end=" ")

print()

from itertools import combinations
data_set = ['a' ,'b' ,'c']
for i in combinations(data_set, 2):
    print("".join(i) ,end=" ")

print()

from itertools import combinations_with_replacement
for idx ,i in enumerate(combinations_with_replacement(['a' ,'b' ,'c'] ,3)):
    print(i, end=" ")

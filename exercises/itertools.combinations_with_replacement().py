from itertools import combinations_with_replacement

inline = input()
string = inline.split()[0]
k = int(inline.split()[1])

list = list(combinations_with_replacement(string, k))
list = sorted(["".join(sorted(element)) for element in list])
for element in list:
    print(element)

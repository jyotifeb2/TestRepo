def is_sorted(li):
    return li == sorted(li)


print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))
print(is_sorted(['a', 'a']))
print(is_sorted(['a', 'b']))
print(is_sorted([2, 1]))
print(is_sorted([1, 2, 3, 4, 3]))
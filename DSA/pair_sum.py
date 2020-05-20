
def pair_sum(lst, k):
    
    if len(lst) < 2:
        return
    seen = set()
    output = set()
    for num in lst:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
           output.add((num, target))
    return len(output)

print pair_sum([1, 3, 2, 2], 4)
assert pair_sum([1, 3, 2, 2], 4) == 2

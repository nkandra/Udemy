# find the missing element in arr2 that is on arr1
#O(nlogn) solution
def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()
    
    # for i in range(len(arr1)-1):
    #     if arr1[i] != arr2[i]:
    #        return arr1[i]
    for num1, num2 in zip(arr1, arr2):
         if num1 != num2:
            return num1
    return arr1[-1]

#O(n) solution
def finder2(arr1, arr2):
    counter = {}
    for num in arr1:
        if num not in counter:
           counter[num] = 1
        else:
           counter[num] += 1
    for num in arr2:
        counter[num] -= 1
    for elem in counter:
        if counter[elem] != 0:
            return elem

#O(n) solution with collections
import collections
def finder3(arr1, arr2):
    d = collections.defaultdict(int)
    for num in arr2:
        d[num] += 1
    for num in arr1:
        if d[num] == 0:
           return num
        else:
           d[num] -= 1

assert finder([1, 3, 4, 5, 2, 6], [1, 2, 3, 4, 5]) == 6
assert finder2([1, 3, 4, 5, 2, 6], [1, 2, 3, 4, 5]) == 6
assert finder3([1, 3, 4, 5, 2, 6], [1, 2, 3, 4, 5]) == 6

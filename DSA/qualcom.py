def problem(arr):
     arr = arr[::-1]
     from itertools import combinations
     n = len(arr) - 1
     comb = combinations(arr, n)
     result = []
     for ele in comb:
         result.append(reduce(lambda a, b: a*b, ele))
     return result

def qualcom_problem(arr):
    product = arr[0]
    result = []
    for ele in arr[1:]:
       product *= ele
    for i in range(len(arr)):
       result.append(product/arr[i])
    return result


# O(n^2) solution
def qualcom_problem2(arr):
    result = []
    for i in range(len(arr)):
        temp = 1
        for ele in arr[:i]+arr[i+1:]:
            temp *= ele
        result.append(temp)
    return result

# O(n) solution 
#Yet to complete



print problem([1,2,3,4,5])
print qualcom_problem([1,2,3,4,5])
print qualcom_problem2([1,2,3,4])


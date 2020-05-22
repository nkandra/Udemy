#In this method, we find the largest continuous sum that is possible in an array

def largest_cont_sum(arr):
    max_sum = cont_sum = arr[0]
    for ele in arr[1:]:
        cont_sum = max(cont_sum+ele, ele)
        max_sum = max(cont_sum, max_sum)
    return max_sum


print largest_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1])

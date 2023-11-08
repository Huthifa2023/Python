#1 def converts all positives to 'big'
# def biggie_size(arr):
#     newarr=[]
#     for i in range(len(arr)):
#         if arr[i] < 1:
#             newarr.append(arr[i])
#         else: newarr.append('big')
#     return newarr
# print(biggie_size([-1,3,5,-5,6,3,-123,234,0]))



#2 count num of positives, and replace it with last element in list
# def count_positives(arr):
#     if len(arr) == 0:
#         return False
#     counter = 0
#     for i in range(len(arr)):
#         if arr[i] > 0:
#             counter+=1
#     arr[len(arr)-1] = counter
#     return arr
# print(count_positives([1,2,-3,-4,5]))



# 3 sum total of values within a list
# def sum_total(arr):
#     summation = 0
#     for i in range(len(arr)):
#         summation += arr[i]
#     return summation
# # print(sum_total([2,1,2]))




#4 return the average of values within list //average = summation/count.values
# def average_func(arr):
#     summation = 0
#     for i in range(len(arr)):
#         summation += arr[i]
#     return summation/len(arr)
# # print (average_func([1,2,3,4]))



# 5 take a list and return the length of the list!!
# def arr_length(arr):
#     counter = 0
#     for i in arr:
#         print(arr[i])
#         counter += 1
#     return counter
# # print(arr_length([1,1,1]))



# 6 return the miinum value of a given array, list empty return False
# def minimum(arr):
#     if not arr:
#         return False
#     min_value = arr[0]
#     for i in range(1,len(arr)):
#         if arr[i] < min_value:
#             min_value = arr[i]
#     return min_value
# # print(minimum([1,2,-4,2,1,5]))


# 7 return the maximum value of a given array, list empty return False
# def maximum(arr):
#     if not arr:
#         return False
#     max_value = arr[0]
#     for i in range(1,len(arr)):
#         if arr[i] > max_value:
#             max_value = arr[i]
#     return max_value
# # print(maximum([1,2,-4,2,1,5]))



#8 function takes list, return dictionary that has (sumTotal, average, minimum, maximum, and length), keys with values
# import statistics
# def ultimate_analysis(arr):
#     if not arr:
#         print('Error, list is empty')
#     about_dict = {'sumTotal': sum(arr), 'average': statistics.mean(arr), 'minimum': min(arr), 'maximum': max(arr), 'length': len(arr) }
#     return about_dict
# print(ultimate_analysis([0,1,1,2]))



#9 function that reverse the list (this can be solved using built in function)
# def reverse_list(arr):
#     i=0
#     j=len(arr)-1
#     while i<j:
#         hold = arr[j]
#         arr[j] = arr[i]
#         arr[i] = hold
#         i+=1
#         j-=1
#     return arr
# print(reverse_list([1,2,3]))

#9 can be solved using slicing:
def reverse_list(arr):
    return arr[::-1]
print(reverse_list([1,2,3,4]))
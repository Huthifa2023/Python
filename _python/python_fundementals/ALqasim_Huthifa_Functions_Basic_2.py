#1 function accepts num argument, return new list --1 , from this num   countdown(5) should return [5,4,3,2,1,0]
# arr=[]
# def countdown(num):
#     for i in range(num,-1,-1):
#         arr.append(i)
#     return arr
# print(countdown(5))


#2 function receive list of two nums, print first and return the second
# def printANDreturn(arr):
#     print(arr[0])
#     return arr[1]
# x = printANDreturn([4,12])
# print(x)


#3 function accepts array, return first value+arr.len
# def firstplus(arr):
#     return  arr[0]+len(arr)
# print(firstplus([1,2,3,4,5]))


#4 def will take, array, if len < 2 retun false, check 2nd value , copy all vlaues that > 2nd value
def GreaterThanSecond(arr):
    if len(arr) < 2:
        return False
    newarr=[]
    for i in range(0, len(arr)):
        if arr[i] > arr[1]:
            newarr.append(arr[i])
    print(len(newarr))
    return newarr
print(GreaterThanSecond([11,4,55,12,2,3,4,5,6]))



#5 def accepts size and value, return newarr that len=size , all values=value

# def Length_Value(size,value):
#     newarr=[]
#     for i in range(size):
#         newarr.append(value)
#     return newarr

# print(Length_Value(5,'ONBON'))
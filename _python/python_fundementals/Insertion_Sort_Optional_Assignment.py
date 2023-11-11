#insertion sort, works by shifiting the value to left, until it becomes sorted relative to all left values
#list = [3,5,7,9,0,2,1,4,6,8]

#pseudo code 
#suppose idex0 is smallest value
#grap index1 and compare it with idex0
#if second value smaller than first value shift, 
#now compair 3rd value with the two left values
#and shift in right place


def insertion_sort(list):
    for i in range(1,len(list)):
        summation = 0
        for j in range(i,-1):
            summation += list[j]
        if list[i] < summation


print(insertion_sort([2,1]))
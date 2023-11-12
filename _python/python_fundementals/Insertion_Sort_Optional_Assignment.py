#Insertion sort is a simple sorting algorithm that works similar to the
#way you sort playing cards in your hands. The array is virtually split into 
#a sorted and an unsorted part. Values from the unsorted part are picked and 
#placed at the correct position in the sorted part.


#To sort an array of size N in ascending order iterate over the array 
#and compare the current element (hold) to its predecessor, if the key 
#element is smaller than its predecessor, compare it to the elements 
#before. Move the greater elements one position up to make space for 
#the swapped element.

def insertion_sort(list):
    if len(list) <= 1:
        print("either list is empty or no need to sort!")
    
    for i in range(1,len(list)):
        j = i-1
        hold = list[i]
        while j>=0 and hold<list[j]:
            list[j+1] = list[j]
            j-=1
        list[j+1] = hold
        
    return list


print(insertion_sort([2,1,-1]))
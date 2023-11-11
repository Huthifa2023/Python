#using selection sort (check the minimum value, replace it in index0, then ignore index0, and check the next minumun value and so on)
#list = [5,4,7,9,0,2,3,1,6,8]

def selection_sort(list):
    for j in range(len(list)):
        min_value = list[j]
        for i in range(j+1,len(list),1):
            if min_value < list[i]:
                pass
            else:
                min_value = list[i]
        x = list.index(min_value)            
        list[j] , list[x] = list[x] , list[j]
    return list
print(selection_sort([5,4,7,9,0,2,3,1,6,8]))
            


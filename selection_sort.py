ar = [9,3,2,4,6,21,11,7,12,15,5,8 ]

def selection_sort(arr):
    for i in range(len(arr)): 
        min_index = i
        for j in range (i+1, len(arr)-1):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i] , arr[min_index] = arr[min_index], arr[i]        
      
selection_sort(ar)

for i in range(len(ar)):
    print("%d" % ar[i])       





    
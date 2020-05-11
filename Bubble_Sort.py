ar = []
num= int(input("Enter the total no. of elements you want to sort:"))
for i in range(num):
    
    val = int(input("Enter the elements: \t"))
    ar.append(val)

def bubble_sort(ar):
    #iteration_count = 0
  for i in range(len(ar)):
    # iterate through unplaced elements
    for idx in range(len(ar)- 1):
      #iteration_count += 1
      if ar[idx] > ar[idx + 1]:
        # replacement for swap function
        ar[idx], ar[idx + 1] = ar[idx + 1], ar[idx]
        #if need to print all the steps of the sorting technique uncomment the below print and then call the function separately 
        #print(ar) 

#bubble_sort(ar)
print("Pre-Sort: {0}".format(ar))
bubble_sort(ar)
print("Post-Sort:{0}".format(ar))


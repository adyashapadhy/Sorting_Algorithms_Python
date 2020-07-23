ar = [9,3,2,4,6,21,11,7,12,15,5,8 ]
"""
num= int(input("Enter the total no. of elements you want to sort:"))
for i in range(num):
    
    val = int(input("Enter the elements: \t"))
    ar.append(val)
"""
def bubble_sort(ar):
    #iteration_count = 0
  for i in range(len(ar)):
    # iterate through unplaced elements
    for j in range(len(ar)- 1):
      #iteration_count += 1
      if ar[j] > ar[j + 1]:
        # replacement for swap function
        ar[j], ar[j + 1] = ar[j + 1], ar[j]
        #if need to print all the steps of the sorting technique uncomment the below print and then call the function separately 
        #print(ar) 

#bubble_sort(ar)

#print("Pre-Sort: {0}".format(ar))
bubble_sort(ar)
#print("Post-Sort:{0}".format(ar))
for i in range(len(ar)):
    print("%d" % ar[i])


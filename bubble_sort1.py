ar = [9,3,2,4,6,21,11,7,12,15,5,8 ]

def bubble_sort(ar):
   
  for i in range(len(ar)):
    
    for j in range(len(ar)- 1):
      
      if ar[j] > ar[j + 1]:
       
        ar[j], ar[j + 1] = ar[j + 1], ar[j]

bubble_sort(ar)

for i in range(len(ar)):
    print("%d" % ar[i])        


    
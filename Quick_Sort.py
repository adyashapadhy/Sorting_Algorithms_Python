

my_list = []
num= int(input("Enter the total no. of elements you want to sort:"))
for i in range(num):
    
    val = int(input("Enter the elements: \t"))
    my_list.append(val)

def partition(sort_list,start, end):
  i = (start-1)
  pivot = sort_list[end]
  for j in range(start,end):
    if sort_list[j] <= pivot:
      i += 1
      sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
  sort_list[i+1],sort_list[end] = sort_list[end], sort_list[i+1]   
  return (i+1)


def quick_sort(sort_list, start, end):
  if start < end:
    part = partition(sort_list, start, end)
    quick_sort(sort_list, start, part-1)
    quick_sort(sort_list, part+1, end)

start = 0
end = len(my_list) - 1
quick_sort(my_list, start, end)
print(my_list)


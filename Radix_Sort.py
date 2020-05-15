my_list = []
num= int(input("Enter the total no. of elements you want to sort:"))
for i in range(num):
    
    val = int(input("Enter the elements: \t"))
    my_list.append(val)

def radix_sort(my_list, base=10):
    if my_list == []:
        return
 
    def key_factory(digit, base):
        def key(my_list, index):
            return ((my_list[index]//(base**digit)) % base)
        return key
    largest = max(my_list)
    exp = 0
    while base**exp <= largest:
        my_list = counting_sort(my_list, base - 1, key_factory(exp, base))
        exp = exp + 1
    return my_list
 
def counting_sort(my_list, largest, key):
    c = [0]*(largest + 1)
    for i in range(len(my_list)):
        c[key(my_list, i)] = c[key(my_list, i)] + 1
 
    # Find the last index for each element
    c[0] = c[0] - 1 # to decrement each element for zero-based indexing
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]
 
    result = [None]*len(my_list)
    for i in range(len(my_list) - 1, -1, -1):
        result[c[key(my_list, i)]] = my_list[i]
        c[key(my_list, i)] = c[key(my_list, i)] - 1
 
    return result


sorted_list = radix_sort(my_list)
print('Sorted list: ', end='')
print(sorted_list)
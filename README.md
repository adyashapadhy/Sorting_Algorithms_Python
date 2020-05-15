# Sorting Algorithms In Python

## BUBBLE SORT

- Compares pairngs of adjacent elements
- Two loops
  - First loop iterates as long as list is unsorted
  - second loop is for comparison of the elements.
- Bubble sort requires multiple passes
- Inner loop takes (N-1) iterations and outer loop takes N iterations where N is the number of elements in the list.
- Big O runtime *O(n(n-1)) = O(n(n)) = O(n^2)*

## MERGE SORT

- *Divide and Conquer Algorithm*
- Major two steps:
  - divide the data in smaaler components(*or runs*)
  - then combine the data into a sorted list(*or merge*)
- We divide the list into halves and then sort each of them
- After both of them are sorted, the halves are compared to each other until a sorted list comes as an output
- In merge sort the best, worst, and average time complexity are all same i.e *O(NLog(N))*  

## QUICK SORT 

- *Comparison sort, where values are ordered by a comparison operation such as > or <*
- Choose a "Pivot" and then compare other elements of the array with the pivot
- Upon comparison the array can be divided into three groups:
  - Sub-array containing elements smaller than pivot
  - The pivot itsef
  - Sub-array elements greater than the pivot
- Runtime efficiency: 
  - worst case = *O(N^2)*
  - Average case = *O(NlogN)*

## RADIX SORT

- *Non-comparison sort*
- There are two different kinds of radix sort 
  - Most Significant Digit or MSD 
  - Least Significant Digit or LSD
- Both types of radix sorts organize data into ten "buckets", one for each digit and the numbers are placed into the buckets based on MSDs and LSDs. 
- The bucketting process is repeated again and again until all numbers are considered.
- Complexity of radix sort is *O(wn)* where n is the length of list and w is the average number of digits teh word-size or *w*
- If one assumes that the length of the list is much larger than the no. of digits, *w* can be treated as a constant factor and thus the performance of radix sort is *O(n)*





# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
	#write your code here
	pivot = arr[low]
    start = low + 1
    end = high
    while (start <= end):
        if arr[start] < pivot:
            start = start +1

        if arr[end] > pivot:
            end = end -1

        if start <=end:
            arr[start], arr[end] = arr[end],arr[start]
    arr[low],arr[end]=arr[end],arr[low]
    return end
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
	
	#write your code here
	if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr,pi+1,high)	
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
	print ("%d" %arr[i]), 
  
 

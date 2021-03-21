# Python program for implementation of MergeSort 
def mergeSort(arr):
  
	#write your code here
	n =len(arr)
    L=[]
    R=[]
    if n < 2:
       return
    else:
        mid = int(n / 2)
        for i in list(range(0,mid)):
            L.append(arr[i])
        for i in list(range(mid,n)):
            R.append(arr[i])
        mergeSort(L)
        mergeSort(R)
        merge(L,R,arr)

def merge(L, R, arr):
    print(f"in merge func {arr}")
    nL = len(L)
    nR = len(R)
    i=j=k=0
    while (i < nL and j < nR):
        if L[i] <= R[j]:
           arr[k] = L[i]
           i = i+1
           k = k+1
        else:
            arr[k] = R[j]
            j = j+1
            k = k+1
    while (i < nL):
       arr[k] = L[i]
       k = k+1
       i = i+1
    while (j < nR):
       arr[k] = R[j]
       k=k+1
       j=j+1

  
# Code to print the list 
def printList(arr): 
	#write your code here
	for i in range(len(arr))
		print(arr[i], end = " ")
		
  
# driver code to test the above code 
if __name__ == '__main__': 
	arr = [12, 11, 13, 5, 6, 7]  
	print ("Given array is", end="\n")	
	printList(arr) 
	mergeSort(arr) 
	print("Sorted array is: ", end="\n") 
	printList(arr) 

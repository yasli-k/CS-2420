def QuickSort(A, low, high):
    if high - low <= 0:
        return A
    
    lmgt = low + 1
    for i in range(low + 1, high + 1):
        if A[i] < A[low]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1
    PivotIndex = lmgt -1
    A[low], A[PivotIndex] = A[PivotIndex], A[low]
    QuickSort(A, low, PivotIndex - 1)
    QuickSort(A, PivotIndex+1, high)
    return A
    
def ModQuickSort(A, low, high):
    if high - low <= 0:
        return A
    mid= (low + high)//2
    A[low], A[mid] = A[mid], A[low]
    
    lmgt = low + 1
    for i in range(low + 1, high + 1):
        if A[i] < A[low]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1
    PivotIndex = lmgt -1
    A[low], A[PivotIndex] = A[PivotIndex], A[low]
    ModQuickSort(A, low, PivotIndex - 1)
    ModQuickSort(A, PivotIndex+1, high)
    return A

def MergeSort(A):
    if len(A) <= 1:
        return A
    L = A[:len(A)//2]
    R = A[len(A)//2:]
    MergeSort(L)
    MergeSort(R)
    #i = left A indx
    #j = right A indx
    #k = merged A indx
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1
    return A
        
    
def main():
    unsorted = [3, 5, 7, 6, 2, 8, 1, 9, 4, 6]
    Q = QuickSort(unsorted.copy(), 0, len(unsorted) -1)
    print("QuickSort:", Q)
 
    MQ = ModQuickSort(unsorted.copy(), 0, len(unsorted) -1)
    print("ModifiedQuickSort:", MQ)
    
    M = MergeSort(unsorted.copy())
    print("MergeSort:", M)
 
if __name__ == "__main__":
    main()
 



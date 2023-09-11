import random


def CreateRandomList(size):
    A =[]
    for i in range(size):
        r = random.randrange(0, size)
        A.append(r)
    return A

def BubbleSort(A):
    changes = True
    while changes == True:
        changes = False
        for i in range(0, len(A) -1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                changes = True
            
def ShakerSort(A):
    changes = True
    while changes == True:
        changes = False
        for i in range(len(A) -2,0,-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                changes = True
        for i in range(0, len(A) -1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                changes = True
            
def CountingSort(A):
    F =[0] * len(A)
    for v in A:
        F[v] += 1
        k = 0
    for j in range(len(F)):
        for q in range(F[j]):
            A[k] = j
            k += 1
    

def main():
    r = CreateRandomList(10)
    
    print("original:",r)
    
    A = r.copy()
    A.sort()
    print("sorted:", A)
    
    A = r.copy()
    BubbleSort(A)
    print("BubbleSort:", A)
    
    B = r.copy()
    ShakerSort(B)
    print("ShakerSort:", B)
    
    C = r.copy()
    CountingSort(C)
    print("CountingSort:", C)
    
    

if __name__ == "__main__":
    main()


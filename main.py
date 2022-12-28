# importing threading module
import threading

# merge algorithm
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    M = [0] * n2
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        M[j] = arr[m + 1 + j]
    i = 0 
    j = 0 
    k = l 

    while i < n1 and j < n2:
        if L[i] <= M[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = M[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = M[j]
        j += 1
        k += 1

# merge sort algorithm
def merge_sort(arr, l, r):
    if l < r:
        m = (l + (r - 1)) // 2

        # creating two threads
        t1 = threading.Thread(target=merge_sort, args=(arr, l, m))
        t2 = threading.Thread(target=merge_sort, args=(arr, m + 1, r))

        # starting two threads and joining
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        # call merge function to merge
        merge(arr, l, m, r)


if __name__ == "__main__":
    # array of integers
    arr = [2,7,8,4,6,2,1,3,4,5,6]

    # passing array to merge function
    merge_sort(arr, 0, len(arr) - 1)

    # printing array
    print(arr)
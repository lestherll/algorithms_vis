def bubble_sort(arr):
    length = len(arr)
    
    for i in range (0, length-1):
        for j in range (0, length-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                yield arr

def insertion_sort(arr):
    pass
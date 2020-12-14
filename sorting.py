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
    length = len(arr)

    for i in range(1, length):
        curr_val = arr[i]
        cur_pos = i

        while cur_pos > 0 and arr[cur_pos-1] > curr_val:
            arr[cur_pos] = arr[cur_pos-1]
            cur_pos -= 1
            
            arr[cur_pos] = curr_val
            yield arr
        
def selection_sort(arr):
    length = len(arr)
    new_arr = []
    for i in range(length):
        min_index = arr.index(min(arr))
        min_value = arr.pop(min_index)
        new_arr.append(min_value)
        yield new_arr
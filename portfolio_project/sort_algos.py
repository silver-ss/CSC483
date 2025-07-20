from function_timer import timer

@timer #wrapper
def selection_sort(arr: list[int]) -> None: 
    """Sort a list of integers in in place with selection sort.

    Iteratively selelct the smallest element in unsorted part of list 
    and move it to the correct position in sorted part of list. 

    Args: 
        arr (list[int]): List of integers to be sorted

    Retruns:
        None
    """
    #For ever index in list starting at 0 set index min to current index
    #Compare to all elements to the right, if smaller element found swap
    for i in range(len(arr) -1):
        index_min = i
        #find smallest element in unsort part of list
        for j in range(i+1, len(arr)):
            if arr[j] < arr[index_min]:
                index_min = j
        #tuple swap when smaller element found
        arr[i], arr[index_min] = arr[index_min], arr[i]

@timer #wrapper
def insertion_sort(arr: list[int]) -> None:
    """Sort a list of integers in ascending order, in place.

    This function implements insertion sort by iterating from 
    the second element to the end of the list and inserting each
    element into the already sorted part by shifting larger values 
    one place to the right until in correct position. 

    Args:
        arr (list[int]): The list of integers to sort, modified in 
        place, no return value. 

    Returns:
        None
    """
    for i in range(1, len(arr)):
        j = i
        # Shift element at arr[j] left until in correct position
        while j > 0 and arr[j] < arr[j - 1]:
            #Swap element j and j-1 when not in correct position
            arr[j], arr[j - 1] = arr[j-1], arr[j]
            j -= 1


def merge(arr: list[int], i: int, j: int, k: int) -> None:
    """Merge two sublist of arr in place.

    Merge the sorted sublist arr[i-j] with the sorted sublist arr[j+1-k]
    to sort i-k

    Args:
        arr (list[int]) list to be sorted
        i (int) Starting index of left sublist
        j (int) End index of left sublist
        k (int) End index of right sublist

    Returns:
        None
    """
    merged_size = k - i +1 
    merged_numbers = [0] * merged_size

    merge_pos = 0
    left_pos = i
    right_pos = j +1

    #add smallest from left or right until either is empty
    while left_pos <= j and right_pos <= k:
        if arr[left_pos] <= arr[right_pos]:
            merged_numbers[merge_pos] = arr[left_pos]
            left_pos += 1
        else:
            merged_numbers[merge_pos] = arr[right_pos]
            right_pos +=1
        merge_pos += 1
    #add all remaining elements from left if not empty
    while left_pos <= j:
        merged_numbers[merge_pos] = arr[left_pos]
        left_pos += 1
        merge_pos += 1
    #add all remaining elements from right if not empty
    while right_pos <= k:
        merged_numbers[merge_pos] = arr[right_pos]
        right_pos += 1
        merge_pos += 1
    #add elements back to inital list in sorted order
    for merge_pos in range(merged_size):
        arr[i + merge_pos] = merged_numbers[merge_pos]

@timer #wrapper
def merge_sort(arr: list[int], i: int, k: int):
    """Recursively sort arr[i-k] in place with merge sort.

    Split the list in half at midpoint sort each side and merge them 
    back together.

    Args:
        arr (list[int]) List to be sorted
        i (int) first index in list to be sorted
        k (int) last index in list to be sorted

    Returns:
        None
    """
    j = 0 # initalize midpoint variable

    if i < k:
        #Update midpoint to split list
        j = (i + k) // 2
        #Recursively call merges sort for left and right halfs of list
        merge_sort(arr, i, j)
        merge_sort(arr, j+1, k)
        #Merge the list parts into sorted order
        merge(arr, i, j, k)

@timer #wrapper
def bubble_sort(arr: list[int]) -> None:
    """Sort a list of integers in place using bubble sort.

    This function repeatedly compares consecutive items, swapping as needed to move larger
    elements to the right.  After each pass the next largest element is in
    its final position.
    ```

    Args:
        arr (list[int]) a list to be sorted in place

    Returns:
        None
    """
    size = len(arr)
    for i in range(0, size - 1):
        #move the largest element left of size - i - 1 to in index size-i-1
        for j in range(0, size - i -1):
            if arr[j] > arr[j+1]:
                #swap items that are in wrong position
                arr[j], arr[j+1] = arr[j+1], arr[j]
import pandas as pd
import random
import time
from functools import wraps


def collect_user_inputs():

    """
    Prompt user for array size and a key.
    Validate size is an integer and positive number.
    Validate key is any integer (negative values allowed).
    """

    # collect array size
    while True:
        try:
            size = int(input("provide an array size > 0 to test linear vs binary search time"))
            #check integer provided is greater than 0
            if size <= 0:
                print("VALUE ERROR: Please provide an integer > 0 Try Again.")
                continue
            break
        # check that value provided for size is any integer
        except ValueError:
            print("TYPE ERROR: Array size must be an integer > 0")
    # collect key value to search for
    while True:
        try:
            key = int(input("provide a integer values to search for"))
            break
        # check that value provided for key is any integer
        except ValueError:
            print("TYPE ERROR: Key value must be an integer")

    return size, key

def create_array(arr_size):

    """
    Return an array of the user provided size populated with 
    uniuqe random integers between 0 and 2x size
    """

    min_int = 0
    array_size = arr_size
    return random.sample(range(min_int, array_size * 2), array_size)


def timer(func):

    """
    wrapper for search function that starts a times, runs the function 
    then ends the times and takes end time - start time to find run_time
    clear wrapper after each iteration. Can collect the last runtime 
    using function.last_run
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # record start time
        start = time.perf_counter()
        # run function
        result = func(*args, **kwargs)
        # stop timer and find runtime
        run_time = time.perf_counter() - start 
        # store run_tim as last run
        wrapper.last_run = run_time
        # pass returned results from function
        return result
    # clear last_run value
    wrapper.last_run = None
    return wrapper

@timer # wrapper
def linear_search(arr, target):

    """
    check each element in array for match with user provided key value
    if match found return index, if not found return -1
    """

    for i,v in enumerate(arr):
        if v == target:
            return i
    return -1

@timer
def binary_search(arr, target):

    """
    Requires arr be an array sorted ascending. 
    """

    n = len(arr) #size of array
    low = 0 #low index of area to be searched
    mid = 0 #mid index to compare
    high = n -1 #high index of area to be searchecd
    #loop until low index passes high index
    while (high >= low):
        #update mid to halfway between low and high
        mid = (high + low) // 2 #int division
        # when target is greater than mid updated move low to mid + 1
        if (arr[mid] < target):
            low = mid + 1
        # when target is less than mid update high to mid - 1
        elif(arr[mid] > target):
            high = mid - 1
        # when target = mid return mid
        else: 
            return mid
    # if target not found return -1
    return -1

def test_cases():
    results = []
    for e in range (1, 16):
        size = 2 ** e
        arr = create_array(size)
        arr.sort()
        key = random.choice(arr)
        #dont print first two warmup runs
        if e <= 2:
            binary_search(arr, key)
            linear_search(arr, key)
            continue
        #after warmup run both searches, grab the run times 
        binary_result = binary_search(arr, key)
        binary_time = binary_search.last_run
        linear_result = linear_search(arr, key)
        linear_time = linear_search.last_run
        # store n, size, index, and search times for each test
        results.append({
            "n": e,
            "size": size,
            "key found at index": binary_result, #either result would work here
            "binary search time(seconds)": binary_time,
            "linear search time(seconds)": linear_time
        })
    # convert to dataframe
    df = pd.DataFrame(results)
    # print result summary table view
    return df.to_string(index=False)

if __name__ == '__main__':

    print("Comparing Linear vs Binary Search on a sorted array")
    print("Example results as n grows shows Binary faster on larger n:")
    print(test_cases())
    print("Test your own example:")
    size, key = collect_user_inputs()
    arr = create_array(size)
    arr.sort()
    binary_index = binary_search(arr,key)
    binary_time = binary_search.last_run
    linear_index = linear_search(arr, key)
    linear_time = linear_search.last_run
    #key not found
    if (binary_index == -1 and linear_index == -1):
        print("key not found")
        print(f"Binary Search took {binary_time:.6f} seconds.")
        print(f"Linear Search took {linear_time:.6f} seconds.")
    # key found
    else:
        print(f"Found key at index {binary_index} with binary search in {binary_time:.6f} seconds.")
        print(f"Found key at index {linear_index} with linear search in {linear_time:.6f} seconds.")

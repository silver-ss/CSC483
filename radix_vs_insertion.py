""" Compare radix vs insertion sort for a user sized array of random integers.

Displays the total time each algorithm took to sort the array in seconds.
User can input an array size to compare radix vs insertion sort times. 
"""

import random
import time
from functools import wraps
from typing import Any, List, Optional


def random_array_generator(n: int) -> List[int]:
    """Generate a list of unique random integers.

    Args:
        n (int): How many integers to generate in list
    
    Returns: 
        sample_list List[int]: A list of `n` unique integers in the range [-9999, 9998]
    """
    return random.sample(range(-9999, 9999), n)

def timer(func):

    """Decorator that measures the execution time of a function

    Wraps the target function, records start and end time to find the
    time elapsed, and saves it in `wrapper.last_run`.

    Args:
        func: The function to be decorated

    Returns:
        The wrapper function. After each call, you can read 
        `wrapped_func.last_run` to get run time in seconds. 

    Attributes:
        last_run (Optional[float]): Time in seconds of the most recent call,
            or None if the function has not yet been called.
    """


    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Inner wrapper that times a single call."""
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
    wrapper.last_run: Optional[float] = None
    return wrapper


def radix_get_length(num: int) -> int: 
    """Find the number of digits in an integer
    
    Args:
        num(int): the integer to count digits from 

    Returns:
        digits(int): number of digits in the integer num
    """
    if num == 0:
        return 1
    digits = 0
    while num != 0:
        digits += 1
        num = int(num / 10)
    return digits

@timer
def radix_sort(arr: list[int]) -> None:
    """Sort a list of integers in ascending order in place using Radix sort.

    Iteratively put numbers in buckets by digit values 
    (ones, tens, hundreds, ...) then recombine. 
    Once sorted by magnitude split negatives, reverse them and
    recombine negatives then positives. 

    Args:
        arr(list[int]) a list of integers to be sorted, modified in place

    Returns:
        None
    """
    # Create a list of 10 lists, one for each digit value 0-9
    buckets: List[List[int]] = [[] for _ in range(10)]

    # Number of passes based on largest absolute value
    max_magnitude = max(max(arr), abs(min(arr)))
    max_digits = radix_get_length(max_magnitude)

    # Initialize exponent value at 1
    exp = 1
    for _ in range(max_digits):
        # Put integers in buckets by current digit value
        for num in arr:
            digit = (abs(num) // exp) % 10
            buckets[digit].append(num)

        # Put integers back into array in bucket order, then clear buckets 
        arr.clear()
        for bucket in buckets:
            arr.extend(bucket)
            bucket.clear()
        # Multiply exponent by ten to increase exponent by 1
        exp *= 10
    
    # Pull out negatives, reverse order and add back at front
    negatives = [n for n in arr if n < 0]
    non_negative = [n for n in arr if n >= 0]
    negatives.reverse()
    arr.clear()
    arr.extend(negatives + non_negative)

@timer
def insertion_sort(arr: list[int]) -> None:
    """
    Sort a list of integers in ascending order, in place.

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

def collect_user_size() -> int:
    """
    Prompt user for a size of list to test sort function.

    Will only accept values between 1 and 19998 to avoid value error
    and oversampling errors since range of random.sample is -9999 to 9999
    value of 19998 will take insertion sort ~ 36 seconds.

    Args:
        None
    
    Returns:
        n (int) number of random integers to put in list
    """
    while True:
        n: int = int(input( "Please provide an integer between 1 and 19998"))
        if n < 1 or n > 19998:
            print("ERROR: Provided integer must be between 1 and 19998")
            continue
        break
    return n

if __name__ == '__main__': 
    test_list_radix = random_array_generator(500)
    test_list_insertion = test_list_radix.copy()
    test_list_radix_expected = sorted(test_list_radix)
    test_list_insertion_expected = sorted(test_list_insertion)

    radix_sort(test_list_radix)
    assert test_list_radix == test_list_radix_expected, f"radix_sort failed: {test_list_radix} != {test_list_radix_expected}"
    insertion_sort(test_list_insertion)
    assert test_list_insertion == test_list_insertion_expected, f"insertion_sort failed: {test_list_insertion} != {test_list_insertion_expected}"
    print("All test passed list sorted by both\n")

    size = collect_user_size()
    a1 = random_array_generator(size)
    a2 = a1.copy()

    print(f"For the unsort list of {size} integers:")
    radix_sort(a1)
    print(f"Radix sort completed in {round(radix_sort.last_run,8)} seconds.")
    insertion_sort(a2)
    print(f"Insertion sort completed in {round(insertion_sort.last_run,8)} seconds.")
    a1.append(1)
    a2.append(1)

    print(f"\nFor the nearly sorted list of {size+1} integers:")
    radix_sort(a1)
    print(f"Radix sort completed in {round(radix_sort.last_run,8)} seconds.")
    insertion_sort(a2)
    print(f"Insertion sort completed in {round(insertion_sort.last_run,8)} seconds.")

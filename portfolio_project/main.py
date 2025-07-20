from sort_algos import (
    selection_sort, 
    insertion_sort,
    merge_sort, 
    bubble_sort
)
from function_timer import timer
from typing import List, Tuple
import pandas as pd
import random


def collect_user_inputs():
    """
    Prompt user for array size
    Validate size is an integer and positive number.

    Args:
        None

    Returns:
        size (int): number of elements to put in list
    """
    # collect array size
    while True:
        try:
            size = int(input("Provide an array size > 1 to compare sort algorithm times"))
            #check integer provided is greater than 0
            if size <= 1:
                print("VALUE ERROR: Please provide an integer > 1 Try Again.")
                continue
            break
        # check that value provided for size is any integer
        except ValueError:
            print("TYPE ERROR: Array size must be an integer > 0")

    return size


def create_list(size: int, min_int: int = 0 ):
    """
    Return an array of the user provided size populated with 
    uniuqe random integers between 0 and 2x size -1.

    Args:
        size (int): number of element in the created list
        min_int (int): smallest value allowed in random sample
            defaults to 0

    Returns:
        List[int]: a list of random unsorted integers, with 'size'' elements
            between 0 and 2x size -1
    """
    return random.sample(range(min_int, size * 2), size)

def test_cases(size: int):
    """
    Generate four lists of length `size` for benchmarking sort algorithms:

      1. random_list: completely random unique integers  
      2. sorted_list: the same list, sorted ascending  
      3. reverse_sorted: the same list, sorted descending  
      4. almost_sorted: like sorted_list but with first/last swapped

    Args:
        size (int): Number of elements in each list; must be >= 1.

    Returns:
        Tuple[
            random_list: List[int],
            sorted_list: List[int],
            reverse_sorted: List[int],
            almost_sorted: List[int]
        ]
    """
    random_list = create_list(size)
    sorted_list = sorted(random_list)
    reverse_sorted = sorted_list[::-1]
    almost_sorted = sorted_list.copy()
    almost_sorted[0], almost_sorted[-1] = almost_sorted[-1], almost_sorted[0]

    return random_list, sorted_list, reverse_sorted, almost_sorted

def run_test(arr: list[int]):
    """
    Test each of the four sort algorithms, store the time they took,
    size of the list, if the sort is accurate in an dataframe.

    Args:
        arr (list[int]): list to be sorted

    Returns:
        df (Pandas DataFrame): results in a table with columns:
            Algorithm - which algorithm results are for
            Size - size of the list that was sorted
            Time - seconds sort algorithm took to complete
            Accurate - if results are sorted properly
    """
    results = []

    for name, func in [
        ("Selection", selection_sort), 
        ("Insertion", insertion_sort),
        ("Merge", merge_sort),
        ("Bubble", bubble_sort)
    ]:
        data = arr.copy()
        if name != 'Merge':
            func(data)
        else:
            func(data, 0, len(arr) - 1)
        accurate = (data == sorted(arr))
        run_time = func.last_run
        results.append({
            'Algorithm': name,
            'Size': len(arr),
            'Time': run_time,
            'Accurate': accurate
        })
    df = pd.DataFrame(results, columns = ['Algorithm', 'Size', 'Time', 'Accurate'])
    return df

def get_results(size):
    master_df = []
    arrays: Tuple[List[int], List[int], List[int], List[int]] = test_cases(size)
    test_labels = ['random', 'sorted', 'reverse_sorted', 'almost_sorted']
    for arr, label in zip(arrays, test_labels):
            result_df = run_test(arr)
            result_df['Test Types:'] = label
            master_df.append(result_df)
    combined_df = pd.concat(master_df, ignore_index = True)
    return combined_df

if __name__ == '__main__':
    test_runs_df = []
    test_sizes = [10,100,1000]
    for n in test_sizes:
        test_runs_df.append(get_results(n))
    show_df = pd.concat(test_runs_df, ignore_index=True)
    pivot_df = show_df.pivot_table(
        index=['Algorithm', 'Size'],
        columns = 'Test Types:',
        values = 'Time'
    )
    print("Initial Test Results in Seconds")
    print(pivot_df.to_string(index = True))


    user_test_n = collect_user_inputs()
    user_df = get_results(user_test_n)
    pivot_user_df =  user_df.pivot_table(
        index=['Algorithm', 'Size'],
        columns = 'Test Types:',
        values = 'Time'
    )
    print("\nUser Results in Seconds")
    print(pivot_user_df.to_string(index = True))
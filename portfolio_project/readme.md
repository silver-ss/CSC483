# Sorting Algorithm Benchmark

This project provides a simple CLI tool for benchmarking four sorting algorithms (Selection, Insertion, Merge, and Bubble sort) across different list configurations.

## Structure

- `function_timer.py`  
  A decorator (`@timer`) that measures and records the time of any function it wraps. Use `unc.last_run` to get the most recent runtime in seconds.

- `sort_algos.py`  
  Implements four in-place sorting functions, each wrapped with the `@timer` decorator:

  - `selection_sort(arr)`
  - `insertion_sort(arr)`
  - `merge_sort(arr, start, end)`
  - `bubble_sort(arr)`

- `main.py`  
  Orchestrates the benchmarking workflow:

  1. Generates test lists (`random`, `sorted`, `reverse_sorted`, `almost_sorted`) for sizes 10, 100, 1000 (configurable).
  2. Applies each sorting algorithm to each test case and records:
     - Algorithm name
     - List size
     - Execution time (seconds)
     - Correctness of the result
  3. Displays results as tables in the console.
  4. Prompts the user for a custom list size and repeats the benchmark.

- `test_bench.ipynb`
    Interactive Jupyter notebook demonstrating how to fun the benchmarks, can visualize results and exports to CSV.

## Requirements

- Python 3.7+  (for pandas)
- `pandas` (for result tables)

## Usage

Run the main script:
`python main.py`
    Follow prompts to suppy a custom list size for additional benchmarks. Results will be printed to console. 
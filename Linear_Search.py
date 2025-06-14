#Input an array and key, return the index of the key in the array
def linearSearch(arr, key):
    for i, element in enumerate(arr):
        if element == key:
            return i
    return -1  # Return -1 if the key is not found in the array
int_array = [3,6,1,4,8,12,5,7,9,2]

def print_results(key):
    index = linearSearch(int_array, key)
    if index == -1:
        print(f"{key} is not in the array.")
    else:
        print(f"{key} is located at index {index}.")
    

print_results(12) # 12 is located at index 5.
print_results(2) # 2 is located at index 9.
print_results(10) # 10 is not in the array.
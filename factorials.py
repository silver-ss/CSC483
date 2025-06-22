def recursive_factorial(n):
    #Base case to exit recursion once n reaches 1
    if (n == 1):
        return 1
    #Recursive case, while n > 1 recursively call the function 
    # reducing n by 1 each time until the base case is hit
    return (n * recursive_factorial(n-1))

def iterative_factorial(n):
    sum = 1
    # loops will run for i = 0 to (n-1)
    for i in range(n):
        #starting with 1 multiply by n - 0, n - 1, n - 2... n - (n-1)
        sum *= (n-i)
    return sum


n = int(input("Input an integer to calculate the factorial: "))
print(f"Using recursion the factorial of {n} is {recursive_factorial(n)}.")
print(f"Using iteration the factorial of {n} is still {iterative_factorial(n)}.")
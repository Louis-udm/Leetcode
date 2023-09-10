

# Define a cache decorator
def cacheit(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper

# Apply the cache decorator to the Fibonacci function
@cacheit
def fibonacci_recursive2(n):
    global call_count
    call_count += 1
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci_recursive2(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

# Example usage:
call_count = 0
n = 10  # Calculate Fibonacci(100)
fib_seq = fibonacci_recursive2(n)
print(fib_seq)  # Output: a list containing the first 101 Fibonacci numbers
print(call_count)

call_count = 0
n = 15  # Calculate Fibonacci(100)
fib_seq = fibonacci_recursive2(n)
print(fib_seq)  # Output: a list containing the first 101 Fibonacci numbers
print(call_count)
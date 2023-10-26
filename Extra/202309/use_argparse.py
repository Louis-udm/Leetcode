import argparse
import json
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime, timedelta


"""
Use argparse, and write a Job submission cli program. 
aurguments are like: "--job-name=XXXX --cpus=4 --mem=4000 --time==1:00 --partition=YYYY --gpus=2" 
key-value can be short or long with = or space, e.g. `-c 4` or `--cpus=4`, and `others` is a list.
"""

def parse_time_input(time_input):
    try:
        hours, minutes = map(int, time_input.split(':'))
        return timedelta(hours=hours, minutes=minutes)
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid time format. Please use the format 'HH:MM'.")

@dataclass
class TimeData:
    time_input: str
    time_delta: timedelta

    def __post_init__(self):
        try:
            hours, minutes = map(int, self.time_input.split(':'))
            self.time_delta = timedelta(hours=hours, minutes=minutes)
        except ValueError:
            raise ValueError("Invalid time format. Please use the format 'HH:MM'.")

@dataclass
class JobSubmission:
    job_name: str = ""
    cpus: int = 0
    gpus: int = 0
    mem: int = 0
    is_model: bool = False
    time: timedelta = field(default_factory=timedelta)
    partition: str = ""
    others: Optional[list] = field(default_factory=list)
    # field default_factory 用于没有数据传入时，默认构造对应的数据
    default_values: dict = field(default_factory=lambda:{"a": 1, "b": 2})

def my_argparse(parameters):
    pass

def run_job(args=None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-j", "--job-name", type=str, required=True, default="model_job")
    parser.add_argument("-c", "--cpus", type=int, required=True)
    parser.add_argument("-g", "--gpus", type=int, required=True)
    parser.add_argument("-m", "--mem", type=int, required=True)
    parser.add_argument("-t", "--time", type=parse_time_input, required=True)
    parser.add_argument("-p", "--partition", type=str, required=True)

    parser.add_argument(
        "--others",
        type=str,
        nargs="+",
        required=False,
        help="other in list",
    )

    parser.add_argument(
        "--data",
        type=json.loads,
        required=False,
        help="data",
    )
    parser.add_argument('--foo', 
        required=False, action='store_const', const=42)

    parser.add_argument("--compress", action="store_true")

    args = parser.parse_args(args=args)
    
    job_submission = JobSubmission(
        job_name=args.job_name,
        cpus=args.cpus,
        mem=args.mem,
        time=args.time,
        partition=args.partition,
        gpus=args.gpus,
        others=args.others,
    )

    print(job_submission)
    print(type(args.time))
    print(job_submission.time.total_seconds())


if __name__ == "__main__":
    run_job()

"""
How to replicate the built-in 'map' function in core Python?
"""
# def custom_map(func, iterable):
#     result = []
#     for item in iterable:
#         result.append(func(item))
#     return result

def custom_map(func, iterable):
    return [func(item) for item in iterable]

# Example usage:
numbers = [1, 2, 3, 4, 5]
squared = custom_map(lambda x: x**2, numbers)
print(squared)  # Output: [1, 4, 9, 16, 25]


"""

1. Write a function for fibonacci sequence
"""
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci_recursive(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

# Example usage:
n = 10
fib_seq = fibonacci_recursive(n)
print(fib_seq)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

"""

How would I improve the speed without touching the function  by using a cache decorator? give me an example.
"""

# Define a cache decorator
def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper

# Apply the cache decorator to the Fibonacci function
@memoize
def fibonacci_recursive2(n):
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
n = 100  # Calculate Fibonacci(100)
fib_seq = fibonacci_recursive2(n)
print(fib_seq)  # Output: a list containing the first 101 Fibonacci numbers

# The Fibonacci function is now memoized, so repeated calls with the same argument are much faster.

"""

2 / 2

Question: Check for the intersection (intersection is from math, meaning the same subset from different sets) of nodes in multiple linked lists
"""

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_intersection(lists):
    # Create a dictionary to store nodes and their frequencies
    node_dict = {}
    # result = []

    # Iterate through each linked list
    for linked_list in lists:
        current = linked_list
        unique_values = set()
        while current:
            if current.value not in unique_values:
                unique_values.add(current.value)
                # Check if the node value is already in the dictionary
                if current.value in node_dict: 
                    node_dict[current.value] += 1
                else:
                    node_dict[current.value] = 1
            # If a node appears in all linked lists, add it to the result
            # if node_dict[current.value] == len(lists):
            #     result.append(current.value)
            current = current.next

    result=[v for k,v in node_dict.items() if v==len(lists)]

    return result

# # Example usage:
# # Create linked lists
# list1 = ListNode(1)
# list1.next = ListNode(2)
# list1.next.next = ListNode(3)

# list2 = ListNode(2)
# list2.next = ListNode(3)
# list2.next.next = ListNode(4)

# list3 = ListNode(3)
# list3.next = ListNode(4)
# list3.next.next = ListNode(5)

# # Find intersection
# lists = [list1, list2, list3]
# intersection = find_intersection(lists)
# print(intersection)  # Output: [3]

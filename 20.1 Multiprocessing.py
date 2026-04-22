
"""Sharing Data Between Processes Using Array and Value"""
import ctypes
import multiprocessing
import os

def square(nums, result, val):
    print(f"From inner function Before changing val values: {val.value}")
    val.value = 3.14

    for idx, val in enumerate(nums):
        result[idx] = val**2

    print(f"From inner function: {result[:]}")

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]

    result = multiprocessing.Array("i", len(nums))
    val = multiprocessing.Value("d", 0)
    p1 = multiprocessing.Process(target=square, args=(nums, result, val), name="Process 1")

    p1.start()
    p1.join()

    print(f"From outer function: {result[:]}")
    print(f"From outer function: {val.value}")


import multiprocessing
import os
import time



def square(nums):
    print(f"Process {multiprocessing.current_process().name} (PID: {os.getpid()}) started squaring.")
    for num in nums:
        time.sleep(1)
        print(f"Square of {num} is: {num**2}")

def cube(nums):
    print(f"Process {multiprocessing.current_process().name} (PID: {os.getpid()}) started cubing.")
    for num in nums:
        time.sleep(1)
        print(f"Cube of {num} is: {num**3}")


if __name__ == '__main__':
    print("Normal Multiprocessing")
    num_lict = [1, 3, 6, 8, 9]
    p1 = multiprocessing.Process(target=square, args=(num_lict,), name="square_process")
    p2 = multiprocessing.Process(target=cube, args=(num_lict,), name="cube_process")

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("*"*50)
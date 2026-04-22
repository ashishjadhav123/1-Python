"""Multiprocessing Pool """

from multiprocessing import Pool
import time

def square(num):
    return num * num


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]

    pool = Pool()
    result = pool.map(square, array)
    print(result)
    pool.close()
    pool.join()


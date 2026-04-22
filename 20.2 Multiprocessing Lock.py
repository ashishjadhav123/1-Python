"""Multiprocessing Lock"""

import multiprocessing
import time

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()


if __name__ == "__main__":
    balance = multiprocessing.Value('d', 200)
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=deposit, args=(balance, lock), name='deposit')
    p2 = multiprocessing.Process(target=withdraw, args=(balance, lock), name='withdraw')

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Balance: {balance.value}")

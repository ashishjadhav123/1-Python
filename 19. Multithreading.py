import time
import threading

def square_num(num_list):
    for num in num_list:
        time.sleep(0.2)
        print(f"Square {num} is: {num**2}")


def cube_num(num_list):
    for num in num_list:
        time.sleep(0.2)
        print(f"Cube {num} is: {num**3}")

num_list = [2, 4, 8, 9, 6]
start_time = time.time()

# square_num(num_list)
# cube_num(num_list)

t1 = threading.Thread(target=square_num, args=(num_list, ))
t2 = threading.Thread(target=cube_num, args=(num_list, ))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Time take to process: {time.time() - start_time}")

print("*"*50)
print("Python Code Example (Race Condition)")
counter = 0

def increase():
    global counter
    for _ in range(100000):
        counter += 1

t1 = threading.Thread(target=increase)
t2 = threading.Thread(target=increase)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Counter Value:", counter)

print("*"*50)
print("How to Fix a Race Condition? (Using Lock)")

counter = 0
loc = threading.Lock()

def increase():
    global counter
    for _ in range(100000):
        with loc:
            counter += 1

t1 = threading.Thread(target=increase)
t2 = threading.Thread(target=increase)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Counter Value with thread Lock:", counter)


print("*"*50)
print("Python Example (Using Semaphore)")

import threading
import time

sem = threading.Semaphore(3)  # allow 3 threads at a time

def access(thread_id):
    with sem:
        print(f"Thread {thread_id} entered")
        time.sleep(2)
        print(f"Thread {thread_id} exited")

threads = []
for i in range(6):
    t = threading.Thread(target=access, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()


print("*"*50)
print("Python Example (Using RLock)")

import threading

lock = threading.RLock()

def outer():
    with lock:
        print("Outer lock acquired")
        inner()

def inner():
    with lock:
        print("Inner lock acquired")

t = threading.Thread(target=outer)
t.start()
t.join()


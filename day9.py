# try:
#     a = 1 / 0
    
# except ZeroDivisionError:
#     print("eeeee")
    
# except IndexError :
#     print("indentation error")
    
# finally:
#     print("a")


# threading 
# while True:
#     print(1)
import time, threading
from threading import Lock

# def time_calc(fun):
#     def wrapper(*args, **kwargs):
#         a = time.time()
#         res = fun()
#         b = time.time()
#         print("time taken for execution ",b-a)
#         return res
#     return wrapper
# a = time.time()
# @time_calc
# def thread1():
#     for i in range(0,5):
#         time.sleep(1)
  
# @time_calc      
# def thread2():
#     for j in range(0, 5):
#         time.sleep(1)
        
# t1 = threading.Thread(target=thread1)
# t2 = threading.Thread(target=thread2)


# t1.start()
# t2.start()

# t1.join()
# t2.join()
# b = time.time()
# print("time taken for entire execution ",b-a)

#race around condition





def thread1(lock):
    global a
    for i in range(0, 100):
        lock.acquire()
        time.sleep(0.01)
        a += 1
        lock.release()
        
def thread2(lock):
    global a
    for i in range(0, 100):
        lock.acquire()
        time.sleep(0.01)
        a += 1
        lock.release()
        
    
def main():
    global a 
    a = 0
    lock = Lock()
    
    t1 = threading.Thread(target=thread1, args=(lock,))
    t2 = threading.Thread(target=thread2, args=(lock,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
if __name__ == "__main__":
   
    for i in range(0, 10):
        main()
        print(f"value of x in iteration {i} - {a}")
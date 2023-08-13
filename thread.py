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
        
# thread1()
# thread2()

# b = time.time()
# print("time taken for entire execution ",b-a)


a = 0

def thread1():
    
    for i in range(0, 100):
        global a
        time.sleep(0.01)
        a += 1
        
        
def thread2():
    
    for i in range(0, 100):
        global a
        time.sleep(0.01)
        a += 1
        
        
    
def main():
    global a 
    a = 0

    
    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
if __name__ == "__main__":
   
    for i in range(0, 10):
        main()
        print(f"value of x in iteration {i} - {a}")
value = 200
# factorial = 1
# global_value = 1

def factorial_function(num):
    
    if (num <= 1):
        return 1
    
    fact =  factorial_function(num - 1) * num 
    return fact

# while (value > 1):
#     factorial = factorial * i
#     value -= 1

# for i in range(1, value+1):
#     factorial = factorial * i
    
# factorial = factorial_function(value)
# print(factorial)


# lambda function 

# c = lambda x: x**2
# print(c(2))


# c = "this is value" if (1 < 0) else "this is not value"
# print(c)
# c = [a for a in range(0, 2000+1) if a % 5 == 0]
# print(c)


from datetime import datetime as dt
import time 

# print(dt.datetime.now())
# print(dt.dt.now())
# print(datetime.dt.now())
print(dt.now())

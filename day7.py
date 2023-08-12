# # decorators
# def custom_decorator(fun):
#     def wrapper(*args, **kwargs):
#         print("before")
#         a = fun(*args, **kwargs)
#         for i in a:
#             print (i)
#         print("after")
#         return a
#     return wrapper

# @custom_decorator
# def sum(range):
#     while(range> 1):
#         yield (range + (range -1))
#         range -= 1
   


# # n = 15
# # :
# a = sum(15)
# for i in a:
#     print(i)



# def main():
#     arr = [1, 2, 4, 5, 6, 8, 9, 10, 11, 15]
#     ele = 11
    
#     start= 0 
#     end = len(arr)+1
#     while start < end:
#         if (ele == arr[(start + end) // 2]):
#             print("element found at index", (start + end) // 2)
#             break
#         elif (ele > arr[(start + end) // 2]):
#             start = (start + end) // 2
#         elif (ele < arr[(start + end) // 2]):
#             end = (start + end) // 2
#     else:
#         print("element not found")
# main()
    

# x = 0
# y = 1
# z = 0
# for i in range(0, n):
#     print(z)
#     x = y
#     y = z
#     z = x+ y



total_number_of_students = int(input("enter total number of students: "))
names = []
for i in range (0, total_number_of_students):
    name = input(f"Enter name of student and marks saparated by ' '  {i}: ").split()
    names.append(name)
    
print(names)


# class School():
#     def __init__(self, classes, students, teachers):
#         print("price")
#         self.classes = classes
        
#     def count_classes(self):
#         print(self.classes)
        
    
#     # classes 
#     # students
#     # teachers

# c = School(classes=10, students=2, teachers=50)
# # c2 = School()
# # c3 = School()

# print(c)
# print(c.count_classes())




# class Animal():
#     def __init__(self, name):
#         self.name = name
        
#     def speak(self, avaj=None):
#         return f"Animal Speaks {avaj}"
        
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name) 
#         self.breed = breed
    
#     def speak(self):
#         return super().speak("bhao")    
       
# class Cat(Animal):
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
        
#     def speak(self):
#         return super().speak("meao")    
        
# a = Animal("cat")
# print(a.speak())
# d = Dog("sheru", "desi")
# print(d.speak())
# c = Cat("tom", "blue")
# print(c.speak())


class A():
    class_a = 10
    
    def __init__(self):
        self.rad = 1
        self._a = 2
        self.__a = 3
        
    def __del__(self):
        print("destructor called")
    
    def method_a(self):
        print("method from A")
      
    @property  
    def area(self):
        return 3.14*(self.rad**2)
    
    @property  
    def radius(self):
        return self.rad
    
    @radius.setter
    def set_radius(self, radius):
        self.rad = radius
        
    def __repr__(self):
        return f"A class with properties {self.radius}, {self.a}"
        
# class B():
#     def __init__(self):
#         pass
    
#     def method_b(self):
#         print("method from b")
        
        
# class C(A, B):
#     def __init__(self):
#         pass
    
#     def method_c(self):
#         print("method from c")
        
        
# c = C()
# c.method_a()
# c.method_b()
# c.method_c()

a = A()
print(a.area)
a.set_radius = 10
print(a.radius)
print(a._a)
print(a.__a)
print(a.__dict__)


#file handeling


# file = open("hello.txt", "r")
# for i in range(0, 5):
#     print(file.readline())
    
# file.close()


with open("hello.txt", "r") as file:
    print(file.readlines())
# pip install virtualenv
# virtualenv <env-name>
# activate


#list functions
a = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 0]
a = list([1, 2, 3, 4, 5 ,6, 7, 8, 9, 0])
print(a)
print(type(a))

#len()
print(len(a))

#append()
a.append(10)
print(a)

#extend()
b = list([11, 12])
a.extend(b)
print(a)

#print(a[0])
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[0:5])
print(a[:5])
print(a[3:])
print(a[:])
print(a[-1])
print(a[-3:-1])

print(a[0:7:2])





#insert()
a.insert(5, [13, 14])
print(a)


# a = [ 
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]    
#      ]
# print(a[1][1])

a.remove(5)
print(a)

print(a.index([13, 14]))

b = a.copy()
b[0] = 2
print(a)
print(b)


last_element = a.pop()
print(a)
print(last_element)

a.reverse()
print(a)


# a.sort()
# print(a)



print()
print("set")
a = {1, 2, 3, 3, 4, 5, 5, 6}
a = set({1, 2, 3, 3, 4, 5, 5, 6})
print(a)
print(type(a))



a = (1, 2, 3, 3, 3, 4, 4 ,5 ,6, 7, 8, 9, 0)
a = tuple([1, 2, 3, 3, 3, 4, 4 ,5 ,6, 7, 8, 9, 0])
print(a)
print(type(a))

a = {
    1: "value",
    2: "value2"
}
a = dict( {
    1: "value",
    2: "value2"
})
print(a)
print(type(a))


# a = 1+2j
# print(type(a))
# complex()


# eval()

a = int(input())
b = int(input())
"""
 +,-,*,**,or, and, /, //
"""
c = input()
print()


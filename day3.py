#dictionary


a = {}
print(a)

## clear()

a.clear()
print(a)

## copy()

b = a.copy()
print(b)

## fromkeys()

keys = ["key1", "key2", "key3"]
values = "value1"
b = a.fromkeys(keys, values)
print(b)
b = {
    "key1": 1,
    "key2": 2,
    "key3": 3
}

## keys()
print(b.keys())

## values()
print(b.values())

print(b.items())



print(b["key1"])

print(b["key2"])


## update the dict

b["key5"] = 5
print(b)


## update()

b.update({"key2": "value"})
print(b)


## pop()

c = b.pop("key2")
print(c)
print(b)





### sets 


a = set([1, 2, 3, 3, 4, 5, 6])
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}
print(a)

### clear() -> clear the set
### copy() --> create a copy of a set


### difference(), difference_update()
# print(a.difference_update(b))
# print(a)

### intersection, intersection_update
print(a.intersection(b))


##disjoint
print(a.isdisjoint(b))


## issubset, issuperset, symmectric_difference, union 


## strings 

a = "bHavSar dAkSh"
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.title())
print(a.swapcase())
print(a.center(20, "*")) # ljust, rjust
print(a.count("dAkSh"))
print(len(a))

print(a.find("dAkSh"))
print(a.replace("dAkSh", "6otu"))
print(a.replace("bHavSar", "6otu"))

## startswith string.startswith("prefix", "start", "end")
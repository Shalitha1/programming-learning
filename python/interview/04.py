#Lists
#lists are ordered
#we can edit the lists after defined
#dupplication values are allowed


numbers_list = [1,2,3,4,4,5]

numbers_list[2] = 10
numbers_list.append(20)
numbers_list.remove(2)

print(numbers_list)

#Tuples
#tuples also ordered list
#tuples are immutable
#tuples also allwes duplicate values

numbers_tuple = (1,2,3,4,4,5)
print(numbers_tuple)

for i in range(len(numbers_tuple)):
    print(numbers_tuple[i])

#Sets
#Sets are onordered
#Sets are mutable
#Sets don't allow duplicates
#sets doesn't support indexing

numbers_set = {1,2,3,4,5,5}
numbers_set.add(40)

print(numbers_set)

#Dictionary
#stores key-value pairs
#maintains insertion order
#mutable
#keys must be unique
#values can be duplicated
#access values through the keys instead of indexes

student = {
    "name": "John",
    "year": 1,
    "city": "colombo"
}

print(student)

student["year"] = 2

print(student)


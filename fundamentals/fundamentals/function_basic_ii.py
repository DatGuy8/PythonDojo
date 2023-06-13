#1
def countdown(i):
    arr = []
    while i >= 0:
        arr.append(i)
        i -=1
    return arr
j = countdown(3)
print(j)

#2
def print_and_return(li):
    print(li[0])
    return(li[1])
x = print_and_return([31,21])
print(x)

#3
def first_plus_length(i):
    a = i[0] + len(i)
    return a
b = first_plus_length([21,31,43,54,12,1,2])
print(b)

#4
def values_greater_than_second(a):
    newlist = []
    if len(a) < 2:
        return False
    for x in range(0,len(a)):
        if a[x] > a[1]:
            newlist.append(a[x])
    print(len(newlist))
    return newlist
b = values_greater_than_second([2,4,1,5,6,7])
print(b)

#5
def length_and_value(a,b):
    nlist = []
    for i in range(0,a):
        nlist.append(b)
    return nlist
b = length_and_value(4,5)
print(b)

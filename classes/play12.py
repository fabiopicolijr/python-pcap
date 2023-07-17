list1 = [1,2,3,4,5,6]
print(list1)
list2 = list1[-1:0:-1]
print(list2)

# Negative step changes a way, slice notation works. It makes the slice be built from the tail of the list. So,
# it goes from the last element to the first element. So [-1:1:-1] will start from last element of the list and will
# end end at 2nd element of list, thus as 0th and 1st are sliced we will be left with 7 elements
my_list = [10, 20, 30]

tup1 = tuple(my_list)   # Convert list → tuple
print(tup1)             # (10, 20, 30)

list1 = list(tup1)      # Convert tuple → list
print(list1)            # [10, 20, 30]

print(type(tup1), tup1)

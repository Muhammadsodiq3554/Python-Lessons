# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)

# set1 = {10, 20, 30, 40, 50, 30}
# for i in set1:
#     if i == 10:
#         print("To'g'ri")
#     else:
#         print("Noto'g'ri")

set1 = {1, 25, 7, 15, 10}
set2 = {1, 5, 7, 15, 10}
set3 = set1.difference(set2)
set1.difference_update(set2)
print(set3)
print(set1)


x = {1, 25, 7, 15, 10}
y = {1, 5, 7, 15, 10}
z = x.intersection(y)
x.intersection_update(y)
a = x.union(y) # union -> 2ta setni birlashtirish uchun ishlatiladi
print(a)
print(z)
print(x)

# symmetric_difference  -> 2ta to'plamda bir xil bo'lmagan elementlarni oladi
# symmetric_difference_update
# a = [1,3,"a",7,"g",8,"q"]
# str_list = []
# number = 0

# for i in a:
#     if type(i) == str:
#         str_list.append()
#     if type(i) == int:
#         number = i + number

# print(str_list, number)


# a = "Salom hammaga yaxshimisizlar guruhdagilar"

# words = a.split()

# b = len(words[1]) + len(words[-1])

# print(b)


yil = int(input("x yilni kiriting: "))
y = yil * 365 * 24 * 3600
s = y * 0.001
print(yil, "yilda", s, "litr suv tomadi.")
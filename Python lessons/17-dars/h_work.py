# Uyga vazifa
# 1. Ushbu listdagi elementlarini ko'paytirib beradigan python funksiyasini yozing.

# def multiple_list(list1):
#     result = 1
#     for i in list1:
#         result *= i
#     return result

# list1 = [8,3,4,2,1]
# print(multiple_list(list1))

# 2. Ushbu string qiymatni teskari shaklda yozib beradigan python dasturini tuzing.

# def reverse_str(string):
#     return string[::-1]

# matn1 = "Everyone"
# print(reverse_str(matn1))

# 3. 1dan 20 gacha bo'lgan sonlarni kvadratini chiqarib beradigann python dasturini tuzung (20 ham kiradi).

# def squares():
#     for i in range(1, 21):
#         print(i**2)

# squares()

# 4. Foydalanuvchi juft son yoki toq sonligini ko'rsatib beradigan python dasturini tuzing.

# def juft_yoli_toq(number):
#     if number % 2 == 0:
#         print("Bu juft son")
#     else:
#         print("Bu toq son")

# number = int(input("Son kiriting: "))
# juft_yoli_toq(number)

# 5. Kichik harflarni qabul qiluvchi va katta harflarni qaytaruvchi python funksiyani tuzing.

# def katta_harf(string):
#     return string.upper()

# string = input("So'z kiriting: ")
# print(katta_harf(string))

# 6. Radiusni qabul qiluvchi va doiraing yuzasini qaytaruvchi python funksiya tuzing.

# import math

# def doiraning_yuzi(radius):
#     return math.pi * radius**2

# radius = float(input("Doiraning radiusini kiriting: "))
# print(doiraning_yuzi(radius))

# 7. Ushbu stringdan barcha a harflarini olib tashlaydigan funksiya tuzing.

# def a_ochirish(string):
#     return string.replace("a", "")

# str1 = "Assalomu aleykum hammaga"
# print(a_ochirish(str1))
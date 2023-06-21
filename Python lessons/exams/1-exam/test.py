# 1. S string berilgan, ushbu stringdagi segmentlar sonini aniqlb beradigan dastur tuzing. Segment belgilarni ketma-ketlikga qo'shib ketishi kerak.

#2. Ikkita string qiymatdagi o'zgaruvchi berilgan. Ushbu stringlarni bir-biriga qo'shib, natijani stringda hosil qiling.

#2.1

# num1 = "11" 
# num2 = "123"
# son1 = int(num1)
# son2 = int(num2)
# s = son1 + son2
# print(s)

#2.2

# num1 = "456"
# num2 = "77"
# son1 = int(num1)
# son2 = int(num2)
# s = son1 + son2
# print(s)

#2.3

# num1 = "0"
# num2 = "0"
# son1 = int(num1)
# son2 = int(num2)
# s = son1 + son2
# print(s)

# 3. Quyidagi 2 ta listdagi xam mavjud bo'lgan elementlarni yangi listda chiqarib beradigan python dasturini tuzing.

# 3.1

# nums1 = [1,2,2,1]
# nums2 = [2,2]
# result = []
# for i in nums1:
#     if i in nums2 and i not in result:
#         result.append(i)
# print(result)

#3.2

# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# result = []
# for i in nums1:
#     if i in nums2 and i not in result:
#         result.append(i)
# print(result)

# 4. Ushbu listdagi elementlarni teskari shaklda yozib beradigan dastur tuzing.

#4.1

# s = ["h","e","l","l","o"]
# a = s[::-1]
# print(a)

# 4.2

# s = ["H","a","n","n","a","h"]
# a = s[::-1]
# print(a)

#5. Foydalanuvchidan so'zni qabul qiladigan va uni teskari shaklda yozib beradigan Python dasturini tuzing.

# str1 = str(input("Teskari chiqarib bermoqchi bo'lgan so'zni kiriting: "))
# print(str1[::-1])

# 6. Str va bo'shliqlardan iborat s o'zgaruvchi berilgan bo'lsa, strdagi oxirgi so'zning uzunligini topib beradigan dastur tuzing.

# 7. Raqamning har bir raqami juft son bo'lgan 100 dan 400 gacha (ikkalasi ham kiritilgan) raqamlarni topish uchun Python dasturini yozing. Olingan raqamlar vergul bilan ajratilgan ketma-ketlikda chop etilishi kerak.

# 8. Nested for orqali quyidagi yulduzchali piramidani hosil qiling.

# for i in range(1, 5):
#     for j in range(i):
#         print('*', end='')
#     print()
# for i in range(5, 0, -1):
#     for j in range(i):
#         print('*', end='')
#     print()

# 9. Quyidagi sonli ketma-ketlikda nechta toq va nechta just sonlar borligini aniqlab beradigan python dasturini tuzing.

# sonlar = (12, 33, 7, 101, 91, 60, 5, 82)
# t_sonlar = 0
# j_sonlar = 0

# for i in sonlar:
#     if i % 2 == 0:
#         j_sonlar += 1
#     else:
#         t_sonlar += 1

# print("Toq sonlar:", t_sonlar, "ta")
# print("Juft sonlar:", j_sonlar, "ta")

# 10. 1 dan 100 gacha bo'lgan sonlarni yig'indisini hisoblab beradigan python dasturini tuzing. (range orqali)

# a = 0
# for i in range(1,101):
#     a = a + i
# print(a)

# 11.
# a = 1
# for i in range(2,10):
#     a = a * i
# print(a)
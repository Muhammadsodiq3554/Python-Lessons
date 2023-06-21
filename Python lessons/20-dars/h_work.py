# 1. try except orqali NameError xatolik beradigan dasturini tuzing.

# try:
#     list1 = [1,2,3,4,5]
#     print(list2[3])
# except NameError:
#     print("Bunday o'zgaruvchi topilmadi.")

# 2.  Foydalanuvchidan 2 ta son so'rasin. 2ta sonni bir-biriga bo'lsin. Agar 2-son 0 bo'lsa try except orqali 0 ga bo'lishdagi xatolikni ko'rsatsin. 

# son1 = int(input("Bo'linuvchini kiriting: "))
# son2 = int(input("Bo'luvchini kiriting: "))
# try:
#     natija = son1 / son2
#     print(natija)
# except ZeroDivisionError:
#     print("Sonni nolga bo'lib bo'lmaydi.")

# 3. Foydalanuvchidan son so'rasin . Agar foydalanuvchi manfiy (-) sonlar kiritsa, dastur iltimos faqat musbat son kiriting. deyishi kerak. Try except orqali bajarasiz.

# try:
#     son = int(input("Iltimos son kiriting: "))
#     if son < 0:
#         raise ValueError("Iltimos, faqat musbat son kiriting.")
# except ValueError as e:
#     print(e)

# 4. Faylni o'qib beradigan dastur tuzing (try except orqali). Agar bunday fayl mavjud bo'lmasa, fayl topilmadi dgan xatolik berishi kerak.

# try:
#     with open("file.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("Fayl topilmadi")

# 5. Sonni ildizini chiqarib beradigan dastur tuzing. Agar son manfiy bo'lsa qiymat noto'g'ri kiritildi db xatolik berilishi kerak.

# try:
#     son = int(input("Iltimos son kiriting: "))
#     if son < 0:
#         raise ValueError("Qiymat noto'g'ri kiritildi")
#     else:
#         print(son ** 0.5)
# except ValueError as e:
#     print(e)
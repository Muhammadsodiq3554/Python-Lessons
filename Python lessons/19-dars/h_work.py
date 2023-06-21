# Uy ishi

# 1. txt faylni o'qish uchun Python dasturini yozing. (funksiya orqali)

# f = open("19-dars/demofile.txt", "r")
# print(f.read())

# 2. test2.txt eng uzun so'zni aniqlab beradigan python dasturini tuzing.

# f = open("19-dars/demofile.txt", "r")
# uzun_soz = ""
# for soz in f.read().split():
#     if len(soz) > len(uzun_soz):
#         uzun_soz = soz
# print(uzun_soz)

# 3. test2.txt faylni o'chirib beradigan python dasturini tuzing

# import os
# os.remove('19-dars/test2.txt')

# 4. test2.txt fayliga "O'zbekiston kelajagi buyuk davlat" matnini qo'shib beradigan python dasturini tuzing.

# with open('19-dars/demofile.txt', 'a') as yangi_file:
#     yangi_file.write("\n O'zbekiston kelajai buyuk davlat")

# 5. With statement dan foydalangan holatda test2.txt faylini o'qib beradigan python dasturini tuzing.

# with open('19-dars/demofile.txt', 'r') as fayl:
#     data = fayl.read()
#     print(data)

# 6. test2.txt faylidan faqat dastlabki 5 ta belgini o'qib beradigan python dasturini tuzing.

# with open('19-dars/demofile.txt','r') as fayl1:
#     data = fayl1.read(5)
#     print(data)
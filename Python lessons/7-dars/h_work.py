# Uyga vazifalar
#1. Python-da ro'yxatni teskarisiga yozib bering.

# list1 = [100, 200, 300, 400, 500]
# print(list1[::-1])

#2. Listdan bo'sh strl arni olib tashlang.

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list1 = list(filter(None, list1))
# print(list1)

#3. Quyidagi Python listga 6000 dan keyin 7000 ni  qoʻshish dasturini yozing.

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)

#4. Sizga ro'yxat berilgan. ["h", "i", "j"] pastki ro'yxatini qtepadagi ro'yxatga qo'shish orqali uni kengaytirish dasturini yozing.

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(sub_list)
# print(list1)

# 5. Ro'yxat berilgan. Ro'yxatdagi 20 qiymatini topish uchun dastur yozing va agar u mavjud bo'lsa, uni 200 bilan almashtiring. Faqat birinchi kelgan 20 ni 200 ga almashtirsin.

# list1 = [5, 10, 15, 20, 25, 50, 20]
# a = list1.index(20)
# list1[a] = 200
# print(list1)
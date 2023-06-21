# 1. To'plam elementlarini listga qo'shing.

# sample_set = {"Sariq", "Yashil", "Qora"}
# sample_list = ["Ko'k", "Oq", "Qizil"]
# sample_set.update(sample_list)
# print(sample_set)

# 2. Ikki to'plamdan bir xil elementlarning yangi to'plamini qaytaring

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set3 = set1.intersection(set2)
# print(set3)

# 3. Takroriy nusxalarni olib tashlash orqali ikkala to'plamdan noyob elementlarga ega yangi to'plamni qaytarish uchun Python dasturini yozing.

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set3 = set1.union(set2)
# print(set3)

# 4. Ikkita Python to'plamini hisobga olgan holda, birinchi to'plamni ikkinchi to'plamda emas, faqat birinchi to'plamda mavjud bo'lgan elementlar bilan yangilash uchun Python dasturini yozing.

# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# set3 = set1.difference(set2)
# print(set3)

# 5. Quyidagi to‘plamdan 10, 20, 30-indexlarinii birdaniga olib tashlash uchun Python dasturini yozing.

# set1 = {10, 20, 30, 40, 50}
# list1 = list(set1)
# list1.pop(1)
# list1.pop(2)
# list1.pop(2)
# set1 = set(list1)
# print(set1)

# 6. A yoki B to'plamida mavjud elementlar to'plamini qaytaring, lekin ikkalasini ham emas.

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set3 = set1.symmetric_difference(set2)
# print(set3)

# 7. Ikki to'plamda umumiy elementlar mavjudligini tekshiring. Ha bo'lsa, umumiy elementlarni ko'rsating.

# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# set1.intersection_update(set2)
# print(set1)

# 8. Umumiy elementlardan tashqari, set2 dan elementlarni qo'shish orqali set1ni yangilang.

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set1 = set1.union(set2) - set1.intersection(set2)
# print(set1)

# 9. set1 va set2 uchun umumiy bo'lmagan elementlarni set1dan olib tashlang

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set1 = set1 - (set1 - set2)
# print(set1)
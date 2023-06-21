# 1. Quyida ikkita ro'yxat keltirilgan. Ularni dictionary ga aylantirish uchun Python dasturini yozing, shunday qilib ro‘yxat 1 elementi kalit, ro‘yxat 2 ning elementi esa qiymat bo‘ladi.

# lst1 = ["Javohir" , "Kevin" , "John"]
# lst2 = [10,20,40]
# dictionary1 = dict(zip(lst1,lst2))
# print(dictionary1)

# 2. Ikkita dictionary ni birlashtirib beradigan python dasturini tuzing.

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# result = {**dict1, **dict2}
# print(result)

# 3. Fizika kalitining  qiymatini ekrangga chiqarib beradigan python dasturini tuzing.

# sampleDict = {
#     "sinf": {
#         "talaba": {
#             "ism": "Tohir",
#             "ballar": {
#                 "fizika": 70,
#                 "tarix": 80
#             }
#         }
#     }
# }

# print(sampleDict['sinf']['talaba']['ballar']['fizika'])

# 4. Quyidagi dictionary dan keltirib o'tilgan qiymatlarni chiqarib, yangi list yaratish uchun Python dasturini yozing.

# sample_dict = {
#     "ism":"Karim",
#     "yosh":"25",
#     "oylik_maosh":8000,
#     "shahar":"Tahkent"
# }

# keys = ["ism", "oylik_maosh"]
# result = {key: sample_dict[key] for key in keys}
# print(result)

# 5. Dictionary dan kalitlar ro'yxatini o'chiring.

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# keys = ["name", "salary"]

# for key in keys:
#     sample_dict.pop(key)

# print(sample_dict)

# 6. Ushbu dictionaryda 200 qiymat bor yoki yo'qligini tekshiradigan dastur yozing.

# sample_dict = {'a': 101, 'b': 200, 'c': 303}

# if 200 in sample_dict.values():
#     print("Ushbu dictionary da 200 qiymat mavjud")
# else:
#     print("Ushbu dictionary da 200 qiymat mavjud emas")

# 7. Quyidagi lug'atda shahar nomini manzilga o'zgartirish dasturni yozing.

# sample_dict = {
#   "ism": "Kevin",
#   "yosh":25,
#   "oylik_maosh": 8000,
#   "shahar": "Tashkent"
# }

# sample_dict["manzil"] = sample_dict.pop("shahar")

# print(sample_dict)

# 8. Ushbu dictionary dan minimum bo'lgan qiymatni olib  beradigan python dasturini tuzing.

# sample_dict = {
#   'Fizika': 82,
#   'Matematika': 65,
#   'Tarix': 75
# }

# min_value = min(sample_dict.values())

# for key in sample_dict:
#     if sample_dict[key] == min_value:
#         print(min_value, "yoki", key)

# 9. Quyidagi lug'atda Johnning maoshini 8500 ga o'zgartirish uchun Python dasturini yozing.

# sample_dict = {
#     'emp1': {'name': 'John', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }

# sample_dict['emp1']['salary'] = 8500

# print(sample_dict)

# 10. Lug'atga kalit qo'shish uchun Python dasturini yozing.

# dict1 = {0: 10, 1: 20}

# dict1[2] = 30
# print(dict1)
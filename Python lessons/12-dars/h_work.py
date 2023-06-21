#1. Tuple ni teskari yozib beradigan dastur tuzing. 

# var1 = (10,20,30,40,50,60)
# var1 = var1[::-1]
# print(var1)

#2. Tuple ichida tuple berilgan. 20 qiymatini olib beradigan Python dasturini yozing. 

# tuple1 = ("Banan", [50, 20, 100], (29, 15, 10))
# print(tuple1[1][1])

#3. Faqatgina 50 qiymatga ega bo'lgan tuple yarating.  

# tuple1 = (50,)

#4. Quyidagi tuple ni to‘rtta o‘zgaruvchiga ajratish dasturini yozing va har bir o‘zgaruvchini ko‘rsating.

# tpl1 = ("Uzbekistan", "USA", "Korea", "Australia")
# (davlat1, davlat2, davlat3, davlat4) = tpl1
# print("davlat1: ", davlat1)
# print("davlat2: ", davlat2)
# print("davlat3: ", davlat3)
# print("davlat4: ", davlat4)

#5. Ikkala tuple almashtiring.

# tuple1 = (33, 44, 55)
# tuple2 = (99, 88, 77)
# tuple1, tuple2 == tuple2, tuple1
# print("tuple1: ", tuple2)
# print("tuple2: ", tuple1)

#6. Quyidagi tupledan 444 va 555 elementlarini yangi tuplega ko‘chirish dasturini yozing.

# tpl1 = (111, 222, 333, 444, 555, 666)
# tpl2 = tpl1[3:5]
# print("tpl2 =", tpl2)

#7. Nested tuple berilgan.  Quyidagi tuple ichidagi ro‘yxatning birinchi elementi 22 ni  2222 ga o‘zgartirish dasturini yozing.

# tuple1 = (11, [22, 33], 44, 55)
# tuple1[1][0] = 2222
# print(tuple1)

#8. Ushbu tuple dagi 30 soni nechi marta takrorlanganligini ko'rsatib beradigan dastur tuzing.

# tuple1 = (30, 10, 60, 70, 50, 30, 48, 30)
# print(tuple1.count(30))

#9. Tupledagi barcha elementlar bir xil yoki yo'qligini tekshirib beradigan dastur tuzing. 

# tuple1 = (45, 45, 45, 45)
# if tuple1 == tuple1:
#     print("Bir xil")
# else:
#     print("Bir xil emas.")
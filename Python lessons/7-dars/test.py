#listlar asosan bitta o'zgaruvchida bir nechta qiymat saqlash uchun ishaltiladi

# [] qavs orqali listlarni yaratib olish mumkin

mevalar = ["olma", "anor", "banan"]
print(mevalar)
print(type(mevalar))

# 2. Listdagi ma'lumotlarni tartiblash mumkin
mevalar = ["olma", "anor", "banan"]
print(mevalar[0])

# 3. Listdagi elementlarni o'zgartirish mumkin
mevalar = ["olma", "anor", "banan"]
mevalar[1] = "uzum"
print(mevalar)

# 4. Listdagi elementlarni o'zgartirish mumkin
mevalar = ["olma", "anor", "banan", "olma"]
print(mevalar[3])
print(mevalar[0])

# 5. List yaratib olish u-n list() funksiyasidan foydalanish mumkin.
mevalar = list(("olma", "anor", "banan"))
print(type(mevalar))

# Listdagi elementlarni qirqib olish
variable1 = [1, "Jafar", True, "Lamborghini", "Tesla", 4]

print(variable1[2])
print(variable1[0:4])
print(variable1[-1])
print(variable1[::-1])
print(variable1[2:])
print(variable1[:3])
print(variable1[-5:-2])
print(variable1[1:4:2])
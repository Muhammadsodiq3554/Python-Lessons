# Tuple


# 1. () qavs yozib olinadi.
# 2. Qiymatlarni o'zgartirib bo'lmaydi.

cars = ("Lamborghini", "Bugatti", "McLaren", "Ferrari")

print(cars[1])
print(type(cars))


yangi1 = list(cars)
yangi1[2] = "Rolls Royce"
cars = tuple(yangi1)
print(cars)


# 3. Tartiblasa bo'ladi
cars = ("Lamborghini", "Bugatti", "McLaren", "Ferrari")
print(cars[3])


# 4. Elementlarni takrorlasa bo'ladi
cars = ("Lamborghini", "Bugatti", "McLaren", "Ferrari", "Bugatti")
print(cars[1])


# Eslatma
mevalar1 = ("Olma",)  # -> bu tuple
mevalar2 = ("Olma")   # -> bu string
mevalar3 = ["Olma"]   # -> bu list

print(type(mevalar1))
print(type(mevalar2))
print(type(mevalar3))

# len() -> tuple ni uzunligini aniqlash uchun ishlatiladi
cars = ("Lamborghini", "Bugatti", "McLaren", "Ferrari", "Bugatti")
print(len(cars))

thistuple = ("apple", "orange", "banana")
thistuple2 = ("cherry",)
s = thistuple+thistuple2
print(s)

tuple1 = ("apple", "orange", "banana")
element = "Cherry"

yangi = list(tuple1)
yangi.append(element)
tuple1 = tuple(yangi)
print(tuple1)


# Unpacking

cars = ("Lamborghini", "Bugatti", "McLaren", "Ferrari", "Bugatti")

(car1,car2,car3,car4,car5) = cars

print(car1)
print(car2)
print(car3)
print(car4)
print(car5)
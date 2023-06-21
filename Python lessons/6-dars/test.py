# bool() -> 
print(10>9)
print(10!=9)

x = 5
ism = "Javohir"

print(bool(x))
print(bool(ism))

#False qaytaradigan holatlar
print(bool(False))
print(bool(None))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#statement

# if -> agar

a = 5

if a == 3:
    print("To'g'ri")

#else -> aks holda


a = 23
b = 13

if a+b >= 36:
    print("True")
else:
    print("Noto'g'ri")

#elif -> agar

a = 33
b = 32

if b>a:
    print("Hello")
elif a == b:
    print("Salom")

# Bitta qatordan foydalanish
if a > b: print("Salom")

x = 2
y = 330
print("A") if x>y else print("B")

# and, or, not

a = 1
b = 2
c = 4

if a > b and c > a:
    print("To'g'ri")
else:
    print("Noto'g'ri")

if a > b or c > a:
    print("To'g'ri")
else:
    print("Noto'g'ri")

if not a > b:
    print("To'g'ri")
else:
    print("Noto'g'ri")


#Nested If

x = 41

if x > 10:
    print("Zo'r")
    if x > 20:
        print("Yaxshi")
    else:
        print("Yomon")
elif x != 30:
    print("O'rtacha")
    if x < 10:
        print("Hello")
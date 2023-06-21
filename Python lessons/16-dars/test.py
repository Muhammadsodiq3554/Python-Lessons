#  Funksiya -> kodni takrorlanishini oldini oladi.
# Funksiya 2 xil turi mavjud :
# 1. Standart(o'zgarmas) funksiya.
print()
len()

# 2. Foydalanuvchi tomonidan yaratilgan funksiya 
# Syntax (Umimiy ko'rinishi)
a = int(input("Birinchi sonni kiriting:"))
b = int(input("Ikkinchi sonni kiriting:"))

def ikkita_sonni_qushish():
    c = a + b
    print(c)


ikkita_sonni_qushish()



# Argument -> funksiya tomonidan qabul qilinadigan qiymat (funksiyani to'ldirib berdigan qiymat)
# 2 ta argument bilan yaratilgan funksiya
def ikkita_sonni_ayirish(son1,son2):
    natija = son1-son2
    print(natija)
    
ikkita_sonni_ayirish(8,5)
ikkita_sonni_ayirish(4,2)


def ikkita_sonni_ayirish(son1=7,son2=1):
    natija = son1-son2
    print(natija)
    
ikkita_sonni_ayirish()
ikkita_sonni_ayirish()



# return -> funksiyaga qiymat qaytarish uchun ishlatiladi

# misol-1
def darajaga_kutarish(son):
    result = son**2  #result = son * son
    return result
print(darajaga_kutarish(3))


# misol-2
def oddiy_funksiya(a):
    return 5*a

print(oddiy_funksiya(4))
print(oddiy_funksiya(6))


# return orqali 0 dan 10 (10 ham kiradi) gacha bo'lgan sonlarni bir-biriga qo'shadigan funksiya 
# yaratib berish kerak.
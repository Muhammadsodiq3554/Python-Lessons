"""# ----- Stringda elementlarni qirqib olish ------ #

ism = "Mening ismim Ulug'bek"
print(ism[0]) # 1-elementni oladi
print(ism[0:10]) # 1-element 9 gacha oladi (10-element kirmidi)
print(ism[0:19:3]) # 1-elementdan  18 gacha oladi (19-kirmidi) va 3 ta element tashiydi
print(ism[2:]) # 2-element dan oxirigacna oladi.
print(ism[:9]) # boshidan 9-elementgacha oladi. (9-element kirmidi)

meva = "Banan"
print(meva[::-1]) # Elementni teskari yozib beradi

# Negative index

mashina = "Lamborghini"
print(mashina[-1]) # oxirgi elementni chiqaradi
print(mashina[-8:-4]) # -8 dan -4 chi elementgacha oladi (-4 kirmaydi)
print(mashina[-10:-5:2]) # -10 dan -5 chi elementgacha ol (-5 kirmaydi)
print(mashina[-10:]) # -10 dan oxirigacha
print(mashina[:-7]) # boshidan -7 elementgacha oladi (-7 kirmidi)
print(mashina[:]) # boshidan oxirigacha oladi"""

name = input ("ismingizni kiriting")
print(len(name)/2)
print(name[0:-1:])
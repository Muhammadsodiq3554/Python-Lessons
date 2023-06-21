# Dictionary (Lug'at)

dict1 = {
    "brand": "Chevrolet",
    "model": "Onix",
    "year": 2022,
    "ranglar": ["oq", "qora", "ko'k", "kulrang"],

}

print(dict1)
print(type(dict1))

#Tartiblasa bo'ladi
x = dict1["model"]
y = dict1.get("brand")
print(x)
print(y)

kalit_suzlar = dict1.keys()
qiymatlar = dict1.values()

print(kalit_suzlar)
print(qiymatlar)



dict1 = {
    "brand": "Chevrolet",
    "model": "Onix",
    "year": 2022,
    "ranglar": ["oq", "qora", "ko'k", "kulrang"],

}

if "ranglar" in dict1:
    print("Xa bu yerda ranglar kalit so'zi bor")
else:
    print("Bu yerda ranglar kalit so'zi yo'q")

# Qiymatlarni o'zgartirish
# 1. Kalit so'zga murojat qilish
student1 = {
    "ism": "Nematulloh",
    "yosh": 11,
    "moshina": "Lada",
    "sinf": 5
}

student1["yosh"] = 12
print(student1)

# 2. update()
student1.update({"sinf": 6})
print(student1)

# Yangi element qo'shish
thisdict = {
    "meva": "olma",
    "rangi": "qizil",
    "davlat": "Uzbekistan"
}

# 1. Kalit so'zga murojaat qilish orqali qo'shish mumkin
thisdict["miqdor"] = 3
print(thisdict)

# 2. update orqali
thisdict.update({"miqdor": 3})
print(thisdict)

# Elementlarni o'chirish
# 1. pop()

thisdict.pop("davlat")
print(thisdict)

# 2. popitem() -> 3.7 version baland versiada oxirgi elementni o'chiradi

thisdict.popitem()
print(thisdict)

# del()

del thisdict['rangi']
print(thisdict)

# clear()

thisdict.clear()
print(thisdict)


thisdict = {
    "meva": "olma",
    "rangi": "qizil",
    "davlat": "Uzbekistan"
}

for i in thisdict.values():
    print(i)

for i in thisdict.keys():
    print(i)

for i in thisdict:
    print(thisdict[i])

# copy()

thisdict2 = thisdict.copy()
print(thisdict2)
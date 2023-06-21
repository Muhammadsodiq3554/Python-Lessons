# Listdagi qo'shimcha funksiyalar

# append()
list1 = [10, 20, 30, 40]
list1.append("Sonlar")
print(list1)

#extend() -> 2 ta listni birlashtiradi

lst1 = [0, 1, 2]
lst2 = [3, 4, 5]

lst1.extend(lst2)
print(lst1)

# count() -> sanash uchun ishlatiladi
meva = ["olma", "anor", "uzum"]
print(meva.count("anor"))

#sort() -> saralab beradi
moshinalar = ["Lamborghini", "Ferrari", "Bugatti", "Chevrolet"]
sonlar = [10, 1, 99, -2, 901]
sonlar.sort()
moshinalar.sort()
print(moshinalar)
print(sonlar)

# reverse() -> teskari qilib beradi
moshinalar = ["Lamborghini", "Ferrari", "Bugatti", "Chevrolet"]
moshinalar.reverse()
print(moshinalar)

# filter() -> filterlab beradi

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# the lambda function returns True for even numbers.
even_numbers_iterator = filter(lambda x: (x%2 == 0), numbers)

#converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)

# clear() -> tozalash
noutbuklar = ["hp", "acer", "apple"]
noutbuklar.clear()
print(noutbuklar)

# pop() -> qaysidir elementni o'chirish (indexni kiritish orqali)
noutbuklar = ["hp", "acer", "apple"]
noutbuklar.pop(2)
print(noutbuklar)

# copy() -> nusxa yaratish

programming_language = ["Python", "Java", "PHP", "C++"]
programming_language2 = programming_language.copy()

print(programming_language2)


# insert() -> kiritish biz etgan joyga
telefonlar = ["Nokia", "Siemens", "Xiaomi", "Samsung"]
telefonlar.insert(2,"Apple")
print(telefonlar)


# remove() -> elementni olib tashlash uchun ishlatiladi (elementni kiritish orqali)
telefonlar = ["Nokia", "Siemens", "Xiaomi", "Samsung", 22]
telefonlar.remove(22)
print(telefonlar)


a = [20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
a.remove(10)
print(a)
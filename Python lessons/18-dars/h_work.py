# Uy ishi
# 1. Lambda yordamida tuple ro'yxatini tartilash uchun Python dasturini yozing.

list1 = [('Ingliz tili', 88), ('Fan', 90), ('Matematika', 97), ('Ijtimoiy fanlar', 82)]

list1.sort(key = lambda x: x[1])

print(list1)

# 2. Kichik harflar bilan boshlanadigan nomlarni olib tashlaganingizdan so'ng, ismlar ro'yxati uzunligini yig'adigan Python dasturini yozing. Lambda funktsiyasidan foydalaning.

my_list = ['banan', 'ananas', 'olma', 'olcha']

my_list.sort(key=lambda x: len(x))

print(my_list)

# 3. Lambda orqali belgilangan sondan ildiz olish uchun python dasturini tuzing. 

x = float(input("Son kiriting:" ))

natija1 = lambda x: x * 2

print("Natija = ", natija1(x))

# 4. Lambda funksiyasi orqali belgilangan sonndan ildiz olish uchun python dasturini yozing.

x = 9

natija2 = lambda x: x ** 0.5

print("Natija = ", natija2(x))

# 5. Quyidagi listni sonlari bo'yicha taritiblab beradigan python dasturini tuzing.

n_programmer = [('Python', 198), ('C', 112), ('R', 67)]

n_programmer.sort(key = lambda x: x[1])

print(n_programmer)
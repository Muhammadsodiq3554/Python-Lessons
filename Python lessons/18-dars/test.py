# Nomsiz funksiya (lambda), fayllar bilan ishlash
# lambda -> kichkina anonim  funksiya, bir nechta argumentlarni qabul qiladi va 1 ta qismda iborat


# Syntax:
# lambda arguments: expression


x = lambda a,b,c: (a*5)+b*c

print(x(2,3,4))


# lambda nimaga kerak ?
# 1) Ichki funksiya sifatida foydalansa bo'ladi

def myfunc(n):
    return lambda a: a*n

my_func2 = myfunc(4)
print(my_func2(5))


# 2) filter(), map() va h.k

list1 = [7,9,10,11,44,66,98,103]

natija = filter(lambda x: x%2 == 0, list1)

print(list(natija))

# 1) Vazifa

list1 = [('Fizika',23),('Ingliz tili',88),('Matematika', 55)]

list1.sort(key=lambda x: x)

print(list1)

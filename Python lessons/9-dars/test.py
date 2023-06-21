# Loop 

# 2 xil: 1.For, 2. While

# for loop -> kod blogini bir necha marta takrorlash uchun ishlatamiz.

cars = ['Lamborghini', 'Bugatti', 'Ferrari']


for a in cars:
    print(a)


for i in "Lamborghini":
    print(i)

# for loop bilan break

mevalar = ['olma', 'anor', 'banan', 'gilos']

for b in mevalar:
    print(b)
    if b == "banan":
        break


# for bilan continue

mevalar = ['olma', 'anor', 'banan', 'gilos']

for x in mevalar:
    if x == "anor":
        continue
    print(x)

# for bilan else
sonlar = [1,2,3,4,5]

if i in sonlar:
    print(i)
else:
    print("Zo'r")


sonlar2 = [1,2,3,4,5,6]

for i in sonlar2:
    if i == 3:
        print(i)
    else:
        print("Yomon")

# Nested for
rang = ['qizil', 'oq', 'qora']
moshinalar = ['lacetti', 'nexia', 'captiva']

for i in rang:
    for j in moshinalar:
        print(i,j)



# pass
raqamlar = [1,2,3,4,5,6,7,8,9,10]


for i in raqamlar:
    natija = 2*i
    print(f"2x{i}={natija}")
    
    
lst1 = [2]
lst2 = [1,2,3,4,5,6,7,8,9,10]


for i in lst1:
    for j in lst2:
        print(f"{i}x{j}={i*j}")


sonlar5 = [1,2,3,4,5,6,7,8,9,10]

for b in sonlar5:
    print(b + b)
sonlar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
i = 0
while i < 20:
    if i % 2 == 0 and i % 3 == 0 and i % 4 == 0:
        print(sonlar[i])
    i += 1


for i in range(1, 100):
    if i % 2 == 0 and i % 3 == 0 and i % 4 == 0:
        print(i)



# Ikkita butun son A va B (A<B) berilgan. Shu sonlar oralig'ida joylashgan barcha butun sonlarni o'sish tartibida toping. (Shu sonlar bilan birgalikda) va ularni soni N ni ham.

son = int(input("Son kiriting: "))
result = 0

for i in range(1, son):
    result += i

print(result)

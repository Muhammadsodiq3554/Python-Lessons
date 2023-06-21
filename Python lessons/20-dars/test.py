# # Try, except, finally
# # try kodni ishlidigan qismi uchun, except try qismi notori bo'lsa ishlidi.

# try:
#     a = 7
#     b = 0
#     natija = a/b
#     print(natija)
# except:
#     print("Nolga bo'lish mumkin emas")

try:
    list1 = [1,2,3,4]
    print(list1[5])
except ZeroDivisionError:
    print("Nolga bo'lish mumkin emas")
except IndexError:
    print("Index dan chiqib ketdingiz.")
except NameError:
    print("Nomini noto'g'ri yozdingiz")


# # try bilan else foydalanish

# try:
#     num = int(input("Sonni kiriting: "))
#     assert num%2 == 0  # assert -> shart True yoki False
#                      # qiymat qaytarishini tekshirib beradi
#     print("Bu juft son")
# except:
#     print("Bu juft son emas")
# else:
#     natija = 1/num
#     print(natija)

# # try bilan finally ishlatilishi

# try:
#     a = 20
#     b = 2
#     natija2 = a/b
#     print(natija2)
# except:
#     print("Bu noto'g'ri ishlatilingan")
# finally:
#     print("Dastur tugadi.")


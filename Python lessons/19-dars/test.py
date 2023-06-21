# Fayllar bilan ishlash

# Mode
#'r' -> read
#'w' -> write
#'a' -> append
#'x' -> create
#'b' -> binary
#'t' -> text
#'+' -> update

file1 = open("19-dars/demofile.txt", 'r')
faylni_uqish = file1.read()
print(faylni_uqish)
file1.close()

#fayl qatda joylashganini aniqlash uchun

import os
print(os.getcwd())


#with .. as orqali o'qib olish

with open('19-dars/demofile.txt','r') as fayl1:
    read_text = fayl1.read()
    print(read_text)


# Fayllar bilan ishlash ('w' -> write rejimi)
with open('19-dars/demofile.txt','w') as yangi_file:
    yangi_file.write("Hello World")
    yangi_file.write("=D")

# Fayllar bilan ishlash ('a' -> append rejimi)

with open('19-dars/demofile.txt', 'a') as yangi_file:
    yangi_file.write("\n Hozir havo 39 gradus.")


# Fayllar bilan ishlash ('x' -> create)
# f = open('19-dars/demofile2.txt','x')

# Fayllarni o'chirish
import os
os.remove('19-dars/demofile2.txt')
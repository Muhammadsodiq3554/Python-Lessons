# 1.
def oddiy_funksiya(ism,yosh):
    natija = f"Mening ismim {ism}. Mening yoshim {yosh}da."
    return natija

print(oddiy_funksiya("Alisher", 26))

# 2.
son1 = int(input("Birinchi sonni kiriting:"))
son2 = int(input("Ikkinchi sonni kiriting:"))

def function_1():
    natija1 = son1+son2
    natija2 = son1*son2
    print("Yig'indisi:",natija1)
    print("Ko'paytmasi",natija2)

function_1()

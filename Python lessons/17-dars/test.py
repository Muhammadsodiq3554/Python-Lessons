# Argument (davomi)
# ARBITARY ARGUMENT (*args) -> agar biz nechta argument kiritishni
# bilmasak argument oldidan * belgisi qo'yiladi

def example_func(*bolalar):
    print("Bizda eng kichkina yoshli bolakay" +' '+ bolalar[2])

example_func("Kamron", "Abdurashid", "Laziz", "Jamshid")

def example_2(**mashinalar):
    print(f"Mening garajimdagi eng qimmat mashina {mashinalar['model1']}")

example_2(model1 = "Lamborghini Urus", model2 = "RollsRoyce Phantom", model3 = "BMW M3", model4 = "")

# Default (o'zgarmas) argument
def my_function(davlat="Uzbekistan"):
    print(f"Mening Vatanim {davlat}")

my_function("Shvetsiya")
my_function("Germaniya")
my_function()
my_function("Korea")


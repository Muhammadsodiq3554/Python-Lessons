# copy()
# dict1 = {"ten": 10, "twenty": 20, "thirty": 30}
# dict2 = {"thirty": 30, "fourty": 40}

# dict3 =  dict1.copy()
# dict3.update(dict2)
# print(dict3)

# misol = {
#     "ism" : "Farhod",
#     "yosh" : 23,
#     "kasbi" : "dasturchi"
# }

# mydictionary = dict(misol)
# print(mydictionary)

# mening_oilam = {
#     'farzand1' : {
#         'ism' : "Akbar",
#         'yosh' : 27,
#         'kasbi' : 'Doktor'
#     },
    
#     'farzand2' : {
#         'ism' : "Doston",
#         'yosh' : 18,
#         'kasbi' : {
#             'kasb1' : 'Oshpaz',
#             'kasb2': 'Haydovchi'
#         }
#     }, 
    
#     'farzand3' : {
#         'ism' : "Shoxakbar",
#         'yosh' : 14,
#         'kasbi' : 'O\'quvchi'
#     }
      
# }

# print(mening_oilam["farzand2"]["kasbi"]["kasb1"])

user = str(input("Davlat nomini kiriting: "))

davlatlar = {
    "O'zbekiston" : "Toshkent", 
    "AQSH" : "Washington", 
    "Rossiya": "Moskva",
    "Tojikiston" : "Dushanbe", 
    "Qirg'iziston" : "Bishkek", 
    "Qozog'iston" : "Nursulton", 
    "Malayziya": "Kuala-Lumpur",
    "Singapur" : "Singapur", 
    "Italiya" : "Rim"
}

keys = ["O'zbekiston", "AQSH", "Rossiya", "Tojikiston", "Qirg'iziston", "Qozog'iston", "Malayziya", "Singapur", "Italiya"]

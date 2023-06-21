countries = { "Uzbekistan" : "Tashkent", 
             "USA" : "Washington", 
             "Russia": "Moscow", 
             "Tajikistan" : "Dushanbe", 
             "Kyrgyzstan" : "Bishkek", 
             "Kazakhstan" : "Nursultan", 
             "Malaysia": "Kuala Lumpur", 
             "Singapore" : "Singapore", 
             "Italy" : "Rome" }

country = input("Davlat nomini kiriting: ")

capital = countries.get(country, 'Bu davlat haqida bizda ma\'lumot mavjud emas.')

print(capital)
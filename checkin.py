#If-else operatori Amaliyot

# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avtolar == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())

# javob = float(input("12x6 nechchiga teng?>>>> "))
# if javob != 72:
#     print('Javob xato!')

# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# if 2023-yil<18:
#     print(f"Yoshingiz {2023-yil}da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz!")

# login = input("Yangi login tanlang: ")
# if len(login)>5: #login uzunligini tekshiramiz
#     print("Login 5 harfdan ko'proq bo'lishi lozim.")

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())

# login = input("Loginingizni kiriting: ")
# if login == 'Admin':
#     print("Xush kelibsiz, Admin!. Foydalanuvchilar ro'yhatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login}")

# son_1 = input("Birinchi sonni kiriting: ")
# son_2 = input("Ikkinchi sonni kiriting: ")
# if son_1 == son_2:
#     print("Sonlar teng!")
# else:
#     print("Rahmat!")

# son_1 = input("Birinchi sonni kiriting: ")
# if int(son_1) >= 0:
#     print("Musbat son!")
# else:
#     print("Manfiy son!")

# import math

# son_1 = input("Birinchi sonni kiriting: ")
# if int(son_1) > 0:
#     x = math.sqrt(int(son_1))
#     print(x)
# else:
#     print("Musbat son kiriting!")

son_1 = input("Birinchi sonni kiriting: ")
if int(son_1) / 2 == 0:
    print("Just son!")
else:
    print("Toq son!")
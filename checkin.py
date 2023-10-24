# a = input('Iltimos, juft son kiriting---> ')
# if int(a)%2!=0:
#     print("Kiritgan soningiz juft emas!")
# else:
#     print("Rahmat!")

# yosh = input("Xurmatli foydalanuvchi, yoshingizni kiriting >>> ")
# yosh = int(yosh)
# if yosh<4 or yosh>60:
#     print("Chipta siz uchun bepul!")
# elif yosh<18:
#     print("Siz uchun chipta narxi 10.000 so'm.")
# else:
#     print("Siz uchun chipta narxi 20.000 so'm.")

# a = input("Siz ikkita son kiritishingiz kerak. Bu yerga ularning birinchisini kiriting >>> ")
# b = input("Siz ikkita son kiritishingiz kerak. Bu yerga ularning ikkinchisini kiriting >>> ")

# a = int(a)
# b = int(b)

# if a==b:
#     print("Sonlar teng.")
# elif a>b:
#     print("Birinchi son katta.")
# else:
#     print("Ikkinchi son katta.")

mahsulotlar = ['sovun', 'un', 'yog\'', 'kolbasa', 'pomidor', 'sabzi', 'kashnich', 'robot', 'futbolka', 'shim']
savat = []

savat.append(input("Sotib olishni xohlagan 3ta mahsulotingiz nomini kiriting. Birinchisi >> ".lower()))
savat.append(input("Sotib olishni xohlagan 3ta mahsulotingiz nomini kiriting. Ikkinchisi >> ".lower()))
savat.append(input("Sotib olishni xohlagan 3ta mahsulotingiz nomini kiriting. Uchinchisi >> ".lower()))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Bizda {mahsulot} mahsuloti bor.")
        else:
            print(f"Bizda {mahsulot} mahsuloti qolmagan.")
else:
    print("Savatni to'ldiring!")
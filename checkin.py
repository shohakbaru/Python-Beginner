# a = input('Iltimos, juft son kiriting---> ')
# if int(a)%2!=0:
#     print("Kiritgan soningiz juft emas!")
# else:
#     print("Rahmat!")

yosh = input("Xurmatli foydalanuvchi, yoshingizni kiriting >>> ")
yosh = int(yosh)
if yosh<4 or yosh>60:
    print("Chipta siz uchun bepul!")
elif yosh<18:
    print("Siz uchun chipta narxi 10.000 so'm.")
else:
    print("Siz uchun chipta narxi 20.000 so'm.")
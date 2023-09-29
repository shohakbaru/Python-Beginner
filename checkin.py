#120dan 1200gacha bo'lgan juft sonlat ro'yxati kerak
juft_sonlar = list(range(120, 1200, 2)) #120dan 1200gacha 2 qadam bilan
#konsolga chiqaramiz
print(juft_sonlar)
#joy tashlaymiz
print("\n\n\n\n\n\n\n\n\n\n\n\n")
#joft_sonlar ro'yxatidagi barcha sonlarni yig'indisini hisoblaymiz
yigindi = sum(juft_sonlar)
print(yigindi)
#ro'yxatdagin eng katta sondan eng kichigini ayiramiz
eng_kichik = min(juft_sonlar)
eng_katta = max(juft_sonlar)
ayirma = eng_katta - eng_kichik
print(ayirma)
#ro'yxatdagi elementlar sonini hisoblaymiz
print(len(juft_sonlar))
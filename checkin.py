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
#boshidan o'rtasidan oxiridan 20ta element
beginning_elements = juft_sonlar[:5]

# Take 20 elements from the middle of the list
middle_elements = juft_sonlar[len(juft_sonlar)//2 - 5:len(juft_sonlar)//2 + 5]

# Take 20 elements from the end of the list
end_elements = juft_sonlar[-5:]

print("Beginning elements:", beginning_elements)
print("Middle elements:", middle_elements)
print("End elements:", end_elements)

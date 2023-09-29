#o'zgarmas ro'yhat yaratamiz
davlatlar = ('Iroq', 'Malaysiya', 'Xitoy', 'Amerika', 'Norvegiya', 'O\'zbekiston')
#ro'yhat uzunligini konsolga chiqaramiz
print(len(davlatlar))
#ro'yhatni tartiblaymiz
#sorted() funksiyasi yordamida tartiblab konsolga chiqaramiz
davlatlar2 = davlatlar[:]
print(sorted(davlatlar2))
#asl ro'yxatni konsolga chiqaramiz
print(davlatlar)
#ro'yhatni reverse() bilan chiqaramiz
davlatlar3 = davlatlar[:]
davlatlar3 = list(davlatlar3)
davlatlar3.reverse()
print(davlatlar3)
#sort() yordamida ro'yhatni copy qilib keyin alifbo bo'yicha chiqaramiz
davlatlar4 = davlatlar[:]
davlatlar4 = list(davlatlar4)
davlatlar4.sort()
print(davlatlar4)
#sort() yordamida ro'yxatni copy qilib alifboga teskari ravishda chiqaramiz
davlatlar5 = davlatlar[:]
davlatlar5 = list(davlatlar5)
davlatlar5.sort(reverse=True)
print(davlatlar5)
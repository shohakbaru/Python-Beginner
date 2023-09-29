#o'zgarmas ro'yxat yaratamiz
toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
#o'zgarmas ro'yxatni oddiy ro'yxatga o'tkizamiz
toys = list(toys)
#Ro'yxatga o'zgartirish kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
#Ro'yxatni yana o'zgarmas ro'yxatga aylantiramiz
toys = tuple(toys)
#konsolga chiqaramiz
print(toys)
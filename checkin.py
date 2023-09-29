#taomlar degan ro'yxat yaratamiz
taomlar = ['somsa', 'tandir', 'kabob', 'manti', 'palov']

#nonushta degan yangi listga taomlardan bir nechta element copy qilamiz
nonushta = [taomlar[0], taomlar[-1]]

#konsolga
print(nonushta)

#nonushta ro'yxatida taomlar kamligi sabab yana 2ta element qo'shamiz
nonushta.append("tuxum")  #>>>> tuxum elementi qo'shildi
nonushta.append("kofe")  #>>>> nonushtalarga kofe qo'shildi

#konsolga
print(nonushta)
print(taomlar)

#nonushta ro'yxatini o'zgarmas ro'yxatga aylantiramiz
nonushta = tuple(nonushta)

#konsolga
print(nonushta)
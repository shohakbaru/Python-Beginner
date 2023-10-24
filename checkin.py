menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']

if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menyu:
            print(f"Menyuda {taom} bor.")
        else:
            print(f"Kechirasiz, menyuda {taom} yo'q.")
else:
    print("Savatingiz bo'sh!")
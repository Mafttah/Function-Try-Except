def kullanici_dogrulama2():
    while True:
        yas = input("Yaşınız: ")
        if not yas:
            print("Boş geçemezsiniz.")
            continue
        try:
            yas = int(yas)
            if yas < 0:
                print("Negatif sayı girmeyiniz.")
                continue
            break
        except ValueError:
            print("Lütfen sayı giriniz!")

    while True:
        isim = input("İsminiz: ")
        if not isim:
            print("İsim alanını boş geçemezsiniz.") 
            continue
        if not all(c.isalpha() or c.isspace() for c in isim):
            print("Buraya harf içeren bir isim giremezsiniz.")
            continue
        if len(isim) > 10:
            print("İsim on karakterden büyük olamaz.")
            continue
        break

    return yas, isim

yas_dogrulandi, isim_dogrulandi = kullanici_dogrulama2()
print(f"Yaşınız: {yas_dogrulandi} Adınız: {isim_dogrulandi}")













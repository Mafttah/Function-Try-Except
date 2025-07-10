def ogrenci():
    while True:
        ad = input("Adınız: ")
        if ad == "":
            print("Adınızı boş geçemezsiniz.")
            print("Başa dönülüyor.")
            continue
        if not ad.strip().isalpha():
            print("Lütfen adınızı kelimelerle giriniz: ")
            print("Başa dönülüyor.")    
        soyad = input("Soyadınız: ")
        if soyad == "":
            print("Adınızı boş geçemezsiniz.")
            print("Başa dönülüyor.")
            continue
        if not soyad.strip().isalpha():
            print("Lütfen soyadınızı kelimelerle giriniz: ")
            print("Başa dönülüyor.")
        yas = input("Yaşınız: ")
        if yas == "": 
            print("Boş geçmeyiniz.")
            print("Başa dönülüyor.")
            continue
        if not yas.strip().isdigit():
            print("Lütfen yaşınızı kelimelerle giriniz: ")
            print("Başa dönülüyor.")
        sifre1 = input("Birinci şifreyi giriniz: ")
        if len(sifre1) < 8:
                print("Hata: Şifre en az 8 karakter olmalıdır.")
                continue
        sifre2 = input("İkinci şifreyi giriniz: ")
        if len(sifre2) < 8:
                print("Hata: Şifre en az 8 karakter olmalıdır.")
                continue
        if not str(sifre1) or not str(sifre2):
            print("Hata: Şifre metin formatında olmalıdır.")
        if sifre1 != sifre2:
            print("Hata: Şifreler birbiriyle eşleşmiyor.")
            print("Tekrar deneyin.")
        note1 = int(input("Birinci notu girin: "))
        note2 = int(input("İkinci notu girin: "))
        note3 = int(input("Üçüncü notu girin: "))
        note4 = int(input("Dördüncü notu girin: "))
        sonuc = note1 + note2 + note3 + note4
        ortalama = sonuc / 4
        break
    try:
        print(f"Adınız: {ad} Soyadınız: {soyad} Yaşınız: {yas} ")
        print(f"Şifreniz: {sifre1}")
        print(f"Öğrenicinin yıl sonu toplam sonucu: {sonuc}")
        print(f"Ortalamanız: {ortalama}")
    except Exception as e:
        print("Bilinmeyen hata {e}")
    except KeyError:
        print("Hatalı giriş.")
    except ValueError:
        print("Yaşınızı girin.")
    
bilgi = ogrenci()
















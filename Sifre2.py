def sifre():
    while True:
        sifre1 = input("Birinci şifreyi giriniz: ")
        if len(sifre1) < 8:
             print("Hata: Şifre en az 8 karakter olmalıdır.")
             continue
        sifre2 = input("Şifreyi yeniden giriniz: ")
        if len(sifre2) < 8:
                print("Hata: Şifre en az 8 karakter olmalıdır.")
                continue
        if not str(sifre1) or not str(sifre2):
                print("Hata: Şifre metin formatında olmalıdır.")
        if sifre1 != sifre2:
                print("Hata: Şifreler birbiriyle eşleşmiyor.")
                print("Tekrar deneyin.")
                continue
        break
    try:
        print(sifre1)
    except TypeError:
            return "Hata: Beklenmeyen bir giriş hatası oluştu."
    except ValueError:
            return "Hata: Beklenmeyen bir değer hatası oluştu."
esitlik = sifre()

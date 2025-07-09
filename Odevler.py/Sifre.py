def sifre(sifre1, sifre2):
    while True:
        try:
            sifre1 = input("Birinci şifreyi giriniz: ")
            if len(sifre1) < 8:
                    print("Hata: Şifre en az 8 karakter olmalıdır.")
                    continue
            sifre2 = input("İkinci şifreyi giriniz: ")
            if len(sifre2) < 8:
                    print("Hata: Şifre en az 8 karakter olmalıdır.")
                    continue
            if not str(sifre1) or not str(sifre2):
                return "Hata: Şifre metin formatında olmalıdır."
            if sifre1 != sifre2:
                print("Hata: Şifreler birbiriyle eşleşmiyor.")
                print("Tekrar deneyin.")
                continue
            break
        except TypeError:
            return "Hata: Beklenmeyen bir giriş hatası oluştu."
        except ValueError:
            return "Hata: Beklenmeyen bir değer hatası oluştu."
        break
esitlik = sifre("bora880!1", "ahmet34!")
print(esitlik)
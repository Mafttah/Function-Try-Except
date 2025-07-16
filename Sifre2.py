def sifre():
    print("Şifre en az 8 karakter, sayı ve özel karakter içermelidir.\n")
    while True:
        sifre1 = input("Birinci şifreyi giriniz: ")
        if len(sifre1) < 8:
                print("Hata: Şifre en az 8 karakter olmalıdır.")   
                continue
        if not all(s.isdigit() for s in sifre):
                print("En az bir rakam kullanmalısınız!")
        ozel_karakter = str.punctuation
        print(ozel_karakter)
        ozel_karakter_var = False
        for karakter in sifre1:
                if karakter in ozel_karakter:
                        ozel_karakter_var = True
        if not ozel_karakter_var:
                print("En az bir tane özel karakter kullanmanız lazım.")

        sifre2 = input("Şifreyi yeniden giriniz: ")
        if len(sifre2) < 8:
                print("Hata: Şifre en az 8 karakter olmalıdır.")
                continue

        # if not str(sifre1) or not str(sifre2):
        #         print("Hata: Şifre metin formatında olmalıdır.")
        if sifre1 != sifre2:
                print("Hata: Şifreler birbiriyle eşleşmiyor.")
                print("Tekrar deneyin.")
                continue
                break
        print(sifre1)
sifre()

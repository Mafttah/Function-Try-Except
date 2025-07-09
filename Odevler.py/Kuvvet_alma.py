def kuvvet_alma(taban, us):
    while True:
            taban = int(input("Bir sayı (taban) girin: "))
            us = int(input("Bir sayı (üs) girin: "))
            sonuc = taban ** us
            try:
                if taban == "":
                    print("Sayı girmelisiniz.")
                if us == "":
                    print("Sayı girmelisiniz.")
                    return taban ** us
                print(f"{taban} üzeri {us} = {sonuc}")
            except TypeError:
                print("Sayı olmayan değer girildi.")
            except ValueError:
                print("Fonksiyona sayısal olmayan bir değer gönderildi.")
            except Exception as e:
                print(f"Beklenmeyen hata: {e}")
            return 

sonuc = (kuvvet_alma(4, 3))
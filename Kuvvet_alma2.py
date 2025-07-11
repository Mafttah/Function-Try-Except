def kuvvet_alma(t):
    while True:
            taban = int(input("Bir sayı (taban) girin: "))
            if not taban == "":
                    print("Sayı girmelisiniz.")
                
            us = int(input("Bir sayı (üs) girin: "))
            if not us == "":
                    print("Sayı girmelisiniz.")
            sonuc = taban ** us
            try:   
                print(f"{taban} üzeri {us} = {sonuc}")
            except TypeError:
                print("Sayı olmayan değer girildi.")
            except ValueError:
                print("Fonksiyona sayısal olmayan bir değer gönderildi.")
            except Exception as e:
                print(f"Beklenmeyen hata: {e}")
            return 

sonuc = kuvvet_alma()




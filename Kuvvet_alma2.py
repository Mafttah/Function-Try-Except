def kuvvet_alma():
    while True:
        try:
            taban = int(input("Bir sayı (taban) girin: "))
            if not taban:
                print("Sayı girmelisiniz.")
            
            us = int(input("Bir sayı (üs) girin: "))
            if not us:
                print("Sayı girmelisiniz.")      
            sonuc = taban ** us   
            print(f"{taban} üzeri {us} = {sonuc}")
        except ValueError:
            print("Hata: Fonksiyona sayısal olmayan bir değer gönderildi.")
        except Exception as e:
            print(f"Beklenmeyen hata: {e}")
        return 

sonuc = kuvvet_alma()




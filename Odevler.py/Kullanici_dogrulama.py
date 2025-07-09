def kullanici_dogrulama(isim, yas):
    while True:
        yas = input("Yaşınız: ")
        if yas == "": 
            print("Boş geçmeyiniz.")
            print("Başa dönülüyor.")
            continue
        isim = input("İsminizi girin: ")
        if isim == "":
            print( "Adınızı boş geçemezsiniz.")
            print( "Başa dönülüyor.")
            continue
        if not isim.isalpha() == "":
            print("Lütfen adınızı kelimelerle giriniz: ")
            print("Başa dönülüyor.")       
        try:
            print(f"İsminiz: {isim}, Yaşınız: {yas}")
        except ValueError:
            print(f"Sayı girmelisiniz.")   
            return  isim, yas
        except TypeError:
            print(f"Bir hata oluştu.")
            return isim, yas
        except NameError:
            print(f"Bir isim girmelisiniz.")
            return isim, yas
        break
     
isim = kullanici_dogrulama("Ahmet",34)

def kullanici_dogrulama():
    try:
        while True:
            yas = input("Yaşınız: ")
            if yas == "": 
                print("Boş geçmeyiniz.")
                print("Başa dönülüyor.")
                continue
            while True:    
                isim = input("İsminizi girin: ")
                if isim == "":
                    print( "Adınızı boş geçemezsiniz.")
                    print( "Başa dönülüyor.")
                    continue
                if not isim.isalpha():
                    print("Lütfen adınızı kelimelerle giriniz: ")
                    print("Başa dönülüyor.")       
                print(f"İsminiz: {isim}, Yaşınız: {yas}")
                break
    except ValueError:
            print(f"Sayı girmelisiniz.")   
            return  isim, yas
    except TypeError:
            print(f"Bir hata oluştu.")
            return isim, yas
    except NameError:
            print(f"Bir isim girmelisiniz.")
            return isim, yas
     
isim = kullanici_dogrulama()
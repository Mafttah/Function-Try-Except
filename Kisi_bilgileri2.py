def kisi_bilgileri():
    while True:
        ad = input("Adınız: ")
        if ad == "":
            print("Adınızı boş geçemezsiniz.")
            print("Başa dönülüyor.")
            continue
        if not ad.strip().isalpha():
            print("Lütfen adınızı kelimelerle giriniz: ")
            print("Başa dönülüyor.")
            continue
        if len(ad) >= 7:
              print("Daha kısa bir ad girmelisiniz.")
              continue
        break
    while True:
        soyad = input("Soyadınız: ")
        if soyad == "":
                print("Adınızı boş geçemezsiniz.")
                print("Başa dönülüyor.")
                continue
        if not soyad.strip().isalpha():
                print("Lütfen soyadınızı kelimelerle giriniz: ")
                print("Başa dönülüyor.")
                continue
        if len(soyad) <= 5:
              print("Daha uzun bir soyad girmelisiniz.")
        break
    while True:    
        yas = input("Yaşınız: ")
        if yas == "": 
                print("Boş geçmeyiniz.")
                print("Başa dönülüyor.")
                continue
        if not yas.strip().isdigit():
                print("Lütfen yaşınızı kelimelerle giriniz: ")
                print("Başa dönülüyor.")
        if int(yas) < 18:
                print("Yaşınız uygun değil.")   
        break     
    try:
            print(f"Adınız: {ad} Soyadınız: {soyad} Yaşınız: {yas}")
    except Exception as e:
            print("Bilinmeyen hata {e}")
    except KeyError:
            print("Hatalı giriş.")
            return
    except ValueError:
            print("Yaşınızı girin.")
            return 
        

sonuc = kisi_bilgileri()
def kisi_bilgileri():
    while True:
        ad = input("Adınız: ")
        if not ad:
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
        if not soyad:
                print("Adınızı boş geçemezsiniz.")
                print("Başa dönülüyor.")
                continue
        if not soyad.strip().isalpha():
                print("Lütfen soyadınızı kelimelerle giriniz: ")
                print("Başa dönülüyor.")
                continue
        if len(soyad) <= 5:
              print("Daha uzun bir soyad girmelisiniz.")
              continue
        break
    
    while True:    
        yas = input("Yaşınız: ")
        if not yas: 
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
    except KeyError:
            print("Hatalı giriş.")
            return
    except ValueError:
            print("Yaşınızı girin.")
    except Exception as e:
            print("Bilinmeyen hata {e}")
            return 
        

sonuc = kisi_bilgileri()
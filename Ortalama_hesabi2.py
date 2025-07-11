def ortalama_hesabi(): 
    while True:    
        try:
            sayi1 = input("Birinci sayıyı girin: ")
            if not sayi1:
                print("Boş geçemezsiniz.")
                continue
            sayi1 = int(sayi1)
        except ValueError as e:
            print(f"Hata: Sayı beklenen girişte harf içeren değer girdiniz.")
            continue  
        except Exception as e:
            print(f"Beklenmeyen hata: {e}")
            continue
        break

    while True: 
        try:         
            sayi2 = input("İkinci sayıyı girin: ")
            if not sayi2:
                print("Boş geçemezsiniz.")
                continue
            sayi2 = int(sayi2)
        except ValueError:
                print(f"Hata: Sayı beklenen girişte harf içeren değer girdiniz.")    
                continue
        except Exception as e:
                print("Beklenmeyen hata:", e)
                continue
        break

    while True: 
        try:      
            sayi3 = input("Üçüncü sayıyı girin: ")
            if not sayi3:
                print("Boş geçemezsiniz.")
                continue
            sayi3 = int(sayi3)
        except ValueError:
            print(f"Hata: Sayı beklenen girişte harf içeren değer girdiniz.")
            continue    
        except Exception as e:
            print("Beklenmeyen hata:", e)
            continue
        break

    while True:
        try:       
            sayi4 = input("Dördüncü sayıyı girin: ")
            if not sayi4:
                print("Boş geçemezsiniz.")
                continue
            sayi4 = int(sayi4)
        except ValueError:
                print(f"Hata: Sayı beklenen girişte harf içeren değer girdiniz.")
                continue    
        except Exception as e:
            print("Beklenmeyen hata:", e)
            continue
        break
    try:
        sonuc = sayi1 + sayi2 + sayi3 + sayi4
        print(f"İşlemin sonucu: {sonuc}")
        ortalama = sonuc / 4
        print(f"İşlemin ortalaması: {ortalama}")
    except Exception as e:
         print(f"Bilinmeyen bir hata oluştu: {e}")    

sonuc = ortalama_hesabi()
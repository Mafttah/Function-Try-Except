def ortalama_hesabi(sayi): 
    try:
        sayi1 = int(input("Birinci sayıyı girin: "))
        sayi2 = int(input("İkinci sayıyı girin: "))
        sayi3 = int(input("Birinci sayıyı girin: "))
        sayi4 = int(input("İkinci sayıyı girin: "))
        sonuc = sayi1 + sayi2 + sayi3 + sayi4
        print("İşlemin sonucu: ",sonuc)
        ortalama = sonuc / 4
        print("İşlemin ortalaması: ",ortalama)
        return
    except ValueError:
        print("Hata")    
    except ZeroDivisionError:
        print("Hata: Liste boş, ortalama hesaplanamaz.")
        return  
    except Exception as e:
        print("Beklenmeyen hata:", e)
        return

sonuc = ortalama_hesabi(10)

def ortalama_hesabi(sayilar): 
    sayilar = [23,45,56,34,9,65]
    try:
        if len(sayilar) == 0:
            print("Liste boş")
            ortalama = sum(sayilar)/len(sayilar)
        print(sayilar)
        print(ortalama)
    except ValueError:
        print("Hata")    
    except ZeroDivisionError:
        print("Hata: Liste boş, ortalama hesaplanamaz.")
        return 
    except TypeError:
        print("Hata: Liste sayısal olmayan bir değer içeriyor.")
        return 
    except Exception as e:
        print("Beklenmeyen hata:", e)
        return

sonuc = ortalama_hesabi(12)
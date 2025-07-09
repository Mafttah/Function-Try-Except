def ortalama_hesabi(sayilar):
    print = input("Sayıları girin:")
    sayi = [ {}, {}, {}, {}]
    sayi = int(sayilar)
    sayi.append(sayilar)
    sayilar [23,45,56,34,9,65]
    try:
        if len(sayilar) == 0:
            print("Liste boş")
            toplam = sum(sayilar)
            print(toplam)
            ortalama = sum(sayilar)/len(sayilar)
        print(ortalama)
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
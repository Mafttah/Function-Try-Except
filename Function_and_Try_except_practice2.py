# fonksiyonun içinde kullanıcıdan 2 sayı al.
# 2 sayıyı birbirine böl
# Gerekli kontrolleri yap
# return ile sonucu gönder


def islem():
    try:
        sayi1 = int(input("Birinci sayıyı giriniz: "))
        sayi2 = int(input("İkinci sayıyı giriniz: "))
        sonuc = sayi1 / sayi2
        return sonuc
    except ValueError:
        print(f"Değer hatası.")
        return None
    except SyntaxError:
        print(f"Yazım hatası.")
        return None
    except TypeError:
        print(f"Girilen değerlerden bir tanesi sayı değil. {sayi1}, {sayi2}")
        return None
    except ZeroDivisionError:
        print(f"Sıfıra böldünüz.")
        return None        
    except Exception as e:
        print("Bilinmeyen bir hata oluştu.")
        return None

islemin_sonucu1 = islem()
print(f"İşlemin sonucu 1: {islemin_sonucu1}")

islemin_sonucu2 = islem()
print(f"İşlemin sonucu 2: {islemin_sonucu2}")

islemin_sonucu3 = islem()
print(f"İşlemin sonucu 3: {islemin_sonucu3}")






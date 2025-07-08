# function recap
# function def python anahtarı ile tanımlanır.

def toplama(sayi1, sayi2):
    return sayi1 + sayi2

def cikarma(sayi1, sayi2):
    if sayi2 > sayi1:
        print("Sonuç eksi çıkacak.")
    return sayi1 - sayi2

def bolme(sayi1, sayi2):
    try:
        bolme_sonucu = sayi1 / sayi2
        return bolme_sonucu
    except ZeroDivisionError:
        print("Sıfıra bölme hatası.")
        return None
    except TypeError:
        print("Sayı olmayan değer gönderildi.")
    except Exception as e:
        print(f"Bilinmeyen bir hata oluştu. {e}")
    
# sonuc = toplama(23,45)
# print(f"İşlemin sonucu {sonuc}")
# print(f"Değişik sonuç alma: {toplama(34,65)}")


# sonuc = cikarma(24,34)
# print(f"Çıkarma sonucu: {sonuc}")
# print(f"Değişik çıkarma işlemi sonucu alma: {cikarma(54,23)}")

# sonuc = bolme(60,15)
# print(f"Bölme sonucu: {sonuc}")
# print(f"Değişik bölme alma sonucu: {bolme(56,4)}")

# sonuc = bolme(3,10)
# print(f"Yapılan işlemin sonucu: {sonuc}")

# sonuc = bolme(56,4)
# print(f"Bölme işlenin sonucu: {sonuc}")

# sonuc = bolme(100,25)
# print(f"Sonuç: {sonuc}")

# sonuc = bolme(45,0)
# if sonuc is not None:
#     print(f"Sonuç: {sonuc}")
# else:
#     print("Sonuç none geldi.")    

sonuc = bolme(45,"a")
if sonuc is not None:
    print(f"Sonuç: {sonuc}")
else:
    print("Sonuç none geldi.") 



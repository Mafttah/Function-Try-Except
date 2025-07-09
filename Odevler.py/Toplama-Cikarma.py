def toplama(sayi1, sayi2):
    while True:
        sayi1 = int(input("Birinci sayıyı girin: "))
        sayi2 = int(input("İkinci sayıyı girin: "))
        if sayi2 > sayi1:
            print("Sonuç eksi çıkacak.")
            continue
        break
    try:
            sonuc = sayi1 + sayi2
            return sonuc
    except ValueError:
            print(f"Değer hatası.")
    return None
def cikarma(sayi1, sayi2):
    while True:
        sayi1 = int(input("Birinci sayıyı girin: "))
        sayi2 = int(input("İkinci sayıyı girin: "))
        if sayi2 > sayi1:
            print("Sonuç eksi çıkacak.")
        try:
            sonuc = sayi1 - sayi2
            return sonuc
        except ValueError:
            print(f"Değer hatası.")
            return None

toplama_sonucu = toplama(23,56)
print(f"Toplama işleminin sonucu: {toplama_sonucu}")

cikarma_sonucu = cikarma(90,34)
print(f"Çıkarma işleminin sonucu: {cikarma_sonucu}")
def toplama():
    while True:
        try:
            print("Toplama işlemi için:")
            sayi1 = int(input("Birinci sayıyı girin: "))
            sayi2 = int(input("İkinci sayıyı girin: "))
            sonuc = sayi1 + sayi2
            return sonuc
        except ValueError:
            print("Değer hatası: Lütfen sayısal değer girin.")
            continue

def cikarma():
    while True:
        try:
            print("Çıkarma işlemi için:")
            sayi1 = int(input("Birinci sayıyı girin: "))
            sayi2 = int(input("İkinci sayıyı girin: "))
            if sayi2 > sayi1:
                print("Sonuç eksi çıkacak.")
            if sayi1 < 0:
                print("Sonuç negatif.")
            if sayi2 < 0:
                print("Sonuç pozitif.")
            sonuc = sayi1 - sayi2
            return sonuc
        except ValueError:
            print("Değer hatası: Lütfen sayısal değer girin.")
            continue

toplama_sonucu = toplama()
print(f"Toplama işleminin sonucu: {toplama_sonucu}")

cikarma_sonucu = cikarma()
print(f"Çıkarma işleminin sonucu: {cikarma_sonucu}")
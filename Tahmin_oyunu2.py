def tahmin_oyunu():
    print("Rastgele Sayı Tahmin Oyunu'na Hoş Geldiniz!")
    print("5 ile 20 arasında bir sayı tutun.")

    while True:
            tahmin = int(input("Tahmininizi girin: "))
            if tahmin < 5 or tahmin > 20:
                print("Hata: Lütfen 5 ile 20 arasında bir sayı girin.")
                continue
            tahmin = hedef
            hedef = 15
            if tahmin == hedef:
                print("Tebrikler! Sayıyı doğru tahmin ettiniz.")
                break
            else:
                print("Yanlış tahmin, tekrar deneyin.")
    try:
        print(hedef)        
    except Exception as e:
            print(f"Beklenmeyen hata: {e}")
    except ValueError:
            print("Hata")

sonuc = tahmin_oyunu()
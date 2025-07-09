import random
def tahmin_oyunu():
    print("Rastgele Sayı Tahmin Oyunu'na Hoş Geldiniz!")
    hedef = random.randint(5, 20)
    print("5 ile 20 arasında bir sayı tuttun.")

    while True:
        try:
            tahmin = int(input("Tahmininizi girin: "))
            if tahmin < 5 or tahmin > 20:
                print("Hata: Lütfen 5 ile 20 arasında bir sayı girin.")
                continue
            tahmin = hedef
            if tahmin == hedef:
                print("Tebrikler! Sayıyı doğru tahmin ettiniz.")
                break
            else:
                print("Yanlış tahmin, tekrar deneyin.")
        except Exception as e:
            print(f"Beklenmeyen hata: {e}")
        except ValueError:
            print("Hata")

sonuc = tahmin_oyunu()
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

def kuvvet_alma(taban, us):
    while True:
            taban = int(input("Bir sayı (taban) girin: "))
            us = int(input("Bir sayı (üs) girin: "))
            sonuc = taban ** us
            try:
                if taban == "":
                    print("Sayı girmelisiniz.")
                if us == "":
                    print("Sayı girmelisiniz.")
                    return taban ** us
                print(f"{taban} üzeri {us} = {sonuc}")
                print(sonuc)
            except TypeError:
                print("Sayı olmayan değer girildi.")
            except ValueError:
                print("Fonksiyona sayısal olmayan bir değer gönderildi.")
            except Exception as e:
                print(f"Beklenmeyen hata: {e}")
            return 

sonuc = (kuvvet_alma(4, 3))







def selamlama():
    try:
        while True:
            secim = input("Nasıl selamlamak istersiniz? -> resmi/gayriresmi: ").strip()
            if secim == "resmi":
                print("Sayın Kullanıcı!, Hoşgelsiniz.")
            elif secim == "gayriresmi":
                print("Merhaba!, Hoşgeldiniz.")
            else:
                print("Hata: Geçersiz seçim! Lütfen 'resmi' veya 'gayriresmi' girin.")
                continue
            break
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu. {e}")      

secim = selamlama()


    
def kullanici_dogrulama(isim, yas):
    while True:
        yas = input("Yaşınız: ")
        if yas == "": 
            print("Boş geçmeyiniz.")
            print("Başa dönülüyor.")
            continue
        isim = input("İsminizi girin: ")
        if isim == "":
            print( "Adınızı boş geçemezsiniz.")
            print( "Başa dönülüyor.")
            continue
        if not isim.isalpha() == "":
            print("Lütfen adınızı kelimelerle giriniz: ")
            print("Başa dönülüyor.")       
        try:
            print(f"İsminiz: {isim}, Yaşınız: {yas}")
        except ValueError:
            print(f"Sayı girmelisiniz.")   
            return  isim, yas
        except TypeError:
            print(f"Bir hata oluştu.")
            return isim, yas
        except NameError:
            print(f"Bir isim girmelisiniz.")
            return isim, yas
        break
     
isim = kullanici_dogrulama("Ahmet",34)



def kelime_uzunlugu(kelime):
    while True:
                kelime = input("Bir kelime girin: ")
                print(len(kelime))
                if not kelime.strip().isalpha():
                    print("Lütfen adınızı kelimelerle giriniz: ")
                    print("Başa dönülüyor.")
                    continue
                break
    return 

kelimenin_uzunlugu = kelime_uzunlugu("Armut")

def ortalama_hesabi(sayilar):
    # print = input("Sayıları girin:")
    # sayi = [ {}, {}, {}, {}]
    # sayi = int(sayilar)
    # sayi.append(sayilar)
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


 

def sifre(sifre1, sifre2):
    while True:
        try:
            sifre1 = input("Birinci şifreyi giriniz: ")
            if len(sifre1) < 8:
                    print("Hata: Şifre en az 8 karakter olmalıdır.")
                    continue
            sifre2 = input("İkinci şifreyi giriniz: ")
            if len(sifre2) < 8:
                    print("Hata: Şifre en az 8 karakter olmalıdır.")
                    continue
            if not (sifre1, str) or not (sifre2, str):
                return "Hata: Şifre metin formatında olmalıdır."
            if sifre1 != sifre2:
                print("Hata: Şifreler birbiriyle eşleşmiyor.")
                print("Tekrar deneyin.")
                continue
            break
        except TypeError:
            return "Hata: Beklenmeyen bir giriş hatası oluştu."
        except ValueError:
            return "Hata: Beklenmeyen bir değer hatası oluştu."
        break
esitlik = sifre("bora880!1", "ahmet341!")
print(esitlik)


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


def kisi_bilgilerini_goster(ad, soyad, yas):
    while True:
        ad = input("Adınız: ")
        if ad == "":
            print("Adınızı boş geçemezsiniz.")
            print("Başa dönülüyor.")
            continue
        if not ad.strip().isalpha():
            print("Lütfen adınızı kelimelerle giriniz: ")
            print("Başa dönülüyor.")
        soyad = input("Soyadınız: ")
        if soyad == "":
                print("Adınızı boş geçemezsiniz.")
                print("Başa dönülüyor.")
                continue
        if not soyad.strip().isalpha():
                print("Lütfen soyadınızı kelimelerle giriniz: ")
                print("Başa dönülüyor.")
        yas = input("Yaşınız: ")
        if int(yas) == "": 
                print("Boş geçmeyiniz.")
                print("Başa dönülüyor.")
                continue
        if not yas.strip().isdigit():
                print("Lütfen yaşınızı kelimelerle giriniz: ")
                print("Başa dönülüyor.")
        try:
            print(f"Adınız: {ad} Soyadınız: {soyad} Yaşınız: {yas}")
        except Exception as e:
            print("Bilinmeyen hata {e}")
        except KeyError:
            print("Hatalı giriş.")
            return
        except ValueError:
            print("Yaşınızı girin.")
            return 
        break
        

sonuc = kisi_bilgilerini_goster("Ahmet", "Bozkurt", 40)
        




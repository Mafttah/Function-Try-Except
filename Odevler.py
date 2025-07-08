# def toplama(sayi1, sayi2):
#     try:
#         sayi1 = int(input("Birinci sayıyı girin: "))
#         sayi2 = int(input("İkinci sayıyı girin: "))
#         return sayi1 + sayi2
#     except ValueError:
#         print(f"Değer hatası.")
#         return None
    
# def cikarma(sayi1, sayi2):
#     try:
#         sayi1 = int(input("Birinci sayıyı girin: "))
#         sayi2 = int(input("İkinci sayıyı girin: "))
#         if sayi2 > sayi1:
#             print("Sonuç eksi çıkacak.")
#         return sayi1 - sayi2
#     except ValueError:
#         print(f"Değer hatası.")
#     return None

# toplama_sonucu = toplama(23,56)
# print(f"Toplama işleminin sonucu: {toplama_sonucu}")

# cikarma_sonucu = cikarma(90,34)
# print(f"Çıkarma işleminin sonucu: {cikarma_sonucu}")


    
# def kullanici_dogrulama(isim, yas):
#     try:
#         yas = int(input("Yaşınızı girin: "))
#         isim = input("İsminizi girin: ")
#         if not isim.isalpha() == "":
#                 if yas < 0:
#                     print(f"Yaş sıfırdan küşük olamaz. ")
#     except ValueError:
#         print(f"Sayı girmelisiniz.")     
#     except NameError:
#         print(f"Bir isim girmelisiniz.")
#         return isim, yas
#     except TypeError:
#         print(f"Bir hata oluştu.")
         

# isim = kullanici_dogrulama("Ahmet",34)


# print(f"Kullanıcı doğrulama: {isim}")


# def kelime_uzunlugu(kelime):
#     while True:
#                 kelime = input("Bir kelime girin: ")
#                 print(len(kelime))
#                 if not kelime.strip().isalpha():
#                     print("Lütfen adınızı kelimelerle giriniz: ")
#                     print("Başa dönülüyor.")
#                     continue
#                 break
#     return 

# kelimenin_uzunlugu = kelime_uzunlugu("Armut")

# def ortalama_hesabi(sayi_listesi):
#     try:
#         sayi_listesi = [10, 20, 30]
#         ortalama = sum(sayi_listesi)
#     except ZeroDivisionError:
#         print("Hata: Liste boş, ortalama hesaplanamaz.")
#         return None
#     except TypeError:
#         print("Hata: Liste sayısal olmayan bir değer içeriyor.")
#         return None
#     except Exception as e:
#         print("Beklenmeyen hata:", e)
#         return ortalama

# sayi_listesi = ortalama_hesabi(23)
# print(f"Ortalama: {sayi_listesi}")
 

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






def kelime_uzunlugu():
    try:
        while True:
                kelime = input("Bir kelime girin: ")
                if not kelime.strip().isalpha():
                    print("Lütfen adınızı kelimelerle giriniz: ")
                    print("Başa dönülüyor.")
                if len(kelime) <= 4:
                    print("Bilgilendirme: kelime en az 4 harf olmalıdır.")
                    continue
                break
        print(f"Girilen kelime: {kelime}, kelimenin uzunluğu: {len(kelime)}")
    except ValueError:
          print("Hata: Harf sayısı hatası")

kelimenin_uzunlugu = kelime_uzunlugu()
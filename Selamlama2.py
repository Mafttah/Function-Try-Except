def selamlama():
    try:
        while True:
            secim = input("Nasıl selamlamak istersiniz? -> resmi/gayriresmi: ").strip()
            # lower: her şekilde küçük harf yapar.
            secim = secim.lower()
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
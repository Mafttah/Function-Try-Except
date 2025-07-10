def ortalama_hesabi(): 
    while True:    
        sayi1 = input("Birinci sayıyı girin: ")
        if not sayi1:
            print("Boş geçemezsiniz.")
            continue
        try:
            sayi1 = int(sayi1)
        except ValueError:
            print("Hata")    
        except ZeroDivisionError:
            print("Hata: Liste boş, ortalama hesaplanamaz.")
        except Exception as e:
            print("Beklenmeyen hata:", e)
            continue
        break

    while True:          
        sayi2 = input("İkinci sayıyı girin: ")
        if not sayi2:
                print("Boş geçemezsiniz.")
                continue
        try:
                sayi2 = int(sayi2)
        except ValueError:
                print("Hata")    
        except ZeroDivisionError:
                print("Hata: Liste boş, ortalama hesaplanamaz.")
        except Exception as e:
                print("Beklenmeyen hata:", e)
                continue
        break

    while True:       
                sayi3 = input("Üçüncü sayıyı girin: ")
                if not sayi3:
                    print("Boş geçemezsiniz.")
                    continue
                try:
                    sayi3 = int(sayi3)
                except ValueError:
                    print("Hata")    
                except ZeroDivisionError:
                    print("Hata: Liste boş, ortalama hesaplanamaz.")
                except Exception as e:
                    print("Beklenmeyen hata:", e)
                    continue
                break

    while True:       
            sayi4 = input("Dördüncü sayıyı girin: ")
            if not sayi4:
                print("Boş geçemezsiniz.")
                continue
            try:
                sayi4 = int(sayi4)
            except ValueError:
                    print("Hata")    
            except ZeroDivisionError:
                print("Hata: Liste boş, ortalama hesaplanamaz.")
            except Exception as e:
                print("Beklenmeyen hata:", e)
                continue
            break
    sonuc = sayi1 + sayi2 + sayi3 + sayi4
    print("İşlemin sonucu: ",sonuc)
    ortalama = sonuc / 4
    print("İşlemin ortalaması: ",ortalama)

sonuc = ortalama_hesabi()
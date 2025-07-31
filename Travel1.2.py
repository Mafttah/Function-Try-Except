def Travel():
    while True:
            print("1. West Europe (England, Scotland, Wales, Ireland,Northern Ireland, France, Belgium, Netherland, Germany, Luxemburg, Switzerland)")
            print("2. Latin Countries (Spain, Portugal, Italy")
            print("3. Scandinavian Countries (Norway, Sweden, Fınland, Denmark)")
            print("4. Middle Europe Czechia, Austria, Slovenia, Slovakia)")
            print("5. Balkans (Greece, Bulgaria, Romania, Montenegro, Makedonia, Serbia, Albania, Croatia, Hungary, Slovenia, Bosnia and Herzegovina)")

            part = input("What is your choice for part of Europe? -> 1,2,3,4,5,5:\n ").strip()

            if not part == "5":
                print("They are not ready.")
                break

            print("1. -> Bulgaria")
            print("2. -> Romania")
            print("3. -> Serbia")
            print("4. -> Greece")
            print("5. -> Croatia")
            print("6. -> Albania")
            print("7. -> Slovenia")
            print("8. -> Montenegro")
            print("9. -> Makedonia")
            print("10. -> Hungary")
            print("11. -> Bosna and Herzegovina\n")

            print("\nYour choice is Balkans. Please choose a country:\n ")
            country = input("Your choice for country? -> 1-11(3):\n ").strip()
            if not country == "3":
                print("They are not ready.")

            print("Your choice is Serbia. Please choose a city:\n ")


            print("1. -> Novi Sad")
            print("2. -> Belgrad")
            print("3. -> Nis")
            print("4. -> Subotica\n")

            city = input("Your choice for city? -> 1-4(4): \n ").strip()
            if not city == "4":
                print("They are not ready.")
                break

            print("Your choice is Subotica. However, you should go Begrad firstly because Subotica doesn't have any airport. For this reason, it takes 3 hours by car from Belgrad to Subotica")

            print("1. -> Franciscan Church")
            print("2. -> Raichle Palace")
            print("3. -> Liberty Square - Main Square\n")

            place = input("Your choice for start place? -> 1-3(1): \n ").strip()
            if not place == "1":
                print("Your choice is Franciscan Church\n")
                print("\n")
            else:
                print("They are not ready.")
                break

            second_place = input("Your choice for start place? -> 2-3(2): \n ").strip()
            if not second_place == "2":
                print("Your choice is Raichle Palace\n")
                print("\n")
            else:
                print("They are not ready.")
                break

            third_place = input("Your choice for start place? -> 3(3): \n ").strip()
            if not third_place == "3":
                print("Your choice is Liberty Square - Main Square\n")
                print("\n")
            else:
                print("They are not ready.")
                break

            print("You have finished visiting Subotica. You can choose the next city.\n")

            print("1. -> Novi Sad")
            print("2. -> Belgrad")
            print("3. -> Nis\n")

            city = input("Your choice for city? -> 1-3(1): \n ").strip()
            if not city == "1":
                print("They are not ready.")
                break

            print("You chose Novi Sad. It takes 3 hours by car. So you can choose a place to start your travel:\n")

            print("1. -> Petrovaradin Fortress")
            print("2. -> Dunavska Street")
            print("3. -> Trg Slobode Square")
            print("4. -> Vladicanski Dvor")
            print("5. -> Furuska Gora\n")

            place = input("Your choice for start place? -> (): \n ").strip()
            if not place == "":
                print("Your choice is \n")
                print("\n")
            else:
                print("They are not ready.")
                break

            second_place = input("Your choice for start place? -> (): \n ").strip()
            if not second_place == "":
                print("Your choice is \n")
                print("\n")
            else:
                print("They are not ready.")
                break

            third_place = input("Your choice for start place? -> (): \n ").strip()
            if not third_place == "":
                print("Your choice is \n")
                print("\n")
            else:
                print("They are not ready.")
                break

            fourth_place = input("Your choice for start place? -> (): \n ").strip()
            if not fourth_place == "":
                print("Your choice is \n")
                print("\n")
            else:
                print("They are not ready.")
                break

            fifth_place = input("Your choice for start place? -> (): \n ").strip()
            if not fifth_place == "":
                print("Your choice is \n")
                print("\n")
            else:
                print("They are not ready.")
                break

            print("You have finished visiting Novi Sad. You can choose the next city.\n")

            print("2. -> Belgrad")
            print("3. -> Nis\n")

            city = input("Your choice for city? -> 2-3(2): \n ").strip()
            if not city == "2":
                print("They are not ready.")
                break

            print("You chose Belgrad. It takes 3 hours by car. So you can choose a place to start your travel:\n")

            print("1. -> Kalemegdan")
            print("2. -> Knez Mihailova Street")
            print("3. -> Church of Saint Sava")
            print("4. -> Republic Square")
            print("5. -> Nikola Tesla Museum")
            print("6. -> Tasmajdan")
            print("7. -> Nova Grad")
            print("8. -> National Museum of Serbia")
            print("9. -> Yugoslavya Museum")
            print("10. -> St. Mark’s Church")
            print("11. -> Kalenic Pijaca")
            print("12. -> Museum of the History of Serbia")
            print("13. -> Terazije Square")
            print("14. -> Nicola Pasic Square")
            print("15. -> Skadarlija Square\n")

            place = input("Your choice for start place? -> (): \n ").strip()
            if not place == "":
                print("Your choice is \n")
                print("\n")
            else:
                print("They are not ready.")
                break

            second_place = input("Your choice for start place? -> (): \n ").strip()
            if not second_place == "":
                print("Your choice is \n")
                print("\n")
            else:
                print("They are not ready.")
                break

            third_place = input("Where do you want to start? -> ():\n ").strip()
            if not third_place == "":
                print("Your choice is \n")
                print("\n")
                break

            forth_place = input("Where do you want to start? -> ():\n ").strip()
            if not forth_place == "":
                print("Your choice is \n")
                print("\n")
                break

            fifth_place = input("Where do you want to start? -> ():\n ").strip()
            if fifth_place == "":
                print("Your choice is \n")
                print("\n")
            else:
                print("They are not ready.")
                break

            sixth_place = input("Where do you want to start? -> ():\n ").strip()
            if sixth_place == "":
                print("Your choice is \n")
                print("\n")
            else:
                print("They are not ready.")
                break

            seventh_place = input("Where do you want to start? -> ():\n ").strip()
            if seventh_place == "":
                print("Your choice is \n")
                print("\n")
            else:
                print("They are not ready.")
                break

            eighth_place = input("Where do you want to start? -> ():\n ").strip()
            if eighth_place == "":
                print("Your choice is \n")
                print("\n")
            else:
                print("They are not ready.")
                break

            ninth_place = input("Where do you want to start? -> ():\n ").strip()
            if ninth_place == "":
                print("Your choice is \n")
                print("\n")
            else:
                print("They are not ready.")
                break

            tenth_place = input("Where do you want to start? -> ():\n ").strip()
            if tenth_place == "":
                print("Your choice is \n")
                print("\n")
            else:
                print("They are not ready.")
                break

            eleventh_place = input("Where do you want to start? -> ():\n ").strip()
            if eleventh_place == "":
                print("Your choice is \n")
                print("\n")
            else:
                print("They are not ready.")
                break

            twelfth_place = input("Where do you want to start? -> ():\n ").strip()
            if twelfth_place == "":
                print("Your choice is \n")
                print("\n")
            else:
                print("They are not ready.")
                break

            thirteenth_place = input("Where do you want to start? -> ():\n ").strip()
            if thirteenth_place == "":
                print("Your choice is \n")
                print("\n")
            else:
                print("They are not ready.")
                break

            fourteenth_place = input("Where do you want to start? -> ():\n ").strip()
            if fourteenth_place == "":
                print("Your choice is \n")
                print("\n")
            else:
                print("They are not ready.")
                break

            fifteenth_place = input("Where do you want to start? -> ():\n ").strip()
            if fifteenth_place == "":
                print("Your choice is \n")
                print("\n")
            else:
                print("They are not ready.")
                break

            print("You have finished visiting Belgrad. You can choose the next city.\n")

            print("3. -> Nis\n")

            city = input("Your choice for city? -> 3(3): \n ").strip()
            if not city == "3":
                print("They are not ready.")
                break

            print("You chose Nis. It takes 6 hours by car. So you can choose a place to start your travel:\n")

            print("1. -> Old Town")
            print("2. -> Skull Tower")
            print("3. -> Nis Castle\n")

            place = input("Your choice for start place? -> (): \n ").strip()
            if not place == "":
                print("Your choice is \n")
                print(" \n")
            else:
                print("They are not ready.")
                break

            second_place = input("Your choice for start place? -> (): \n ").strip()
            if not second_place == "":
                print("Your choice is \n")
                print(" \n")
            else:
                print("They are not ready.")
                break

            third_place = input("Where do you want to start? -> ():\n ").strip()
            if not third_place == "":
                print("Your choice is \n")
                print("\n")
                break

            print("1. -> Bulgaria")
            print("2. -> Romania")
            print("4. -> Greece")
            print("5. -> Croatia")
            print("6. -> Albania")
            print("7. -> Slovenia")
            print("8. -> Montenegro")
            print("9. -> Makedonia")
            print("10. -> Hungary")
            print("11. -> Bosna and Herzegovina\n")

            print("Your choice is Balkans. Please choose a country:")
            country = input("You have finished travelling Serbia. You can choose other country. Where to next? -> 1-11(2):\n ").strip()
            if not country == "2":
                print("They are not ready.")

            print("Your choice is Romania. Please choose a city:\n ")

            print("1. -> Bucharest")
            print("2. -> Kostence")
            print("3. -> Transilvanya")
            print("4. -> Kaloşvar")
            print("5. -> Sighișoara")
            print("6. -> Brasov\n")

            city = input("Your choice for city? -> 1-6(2): \n ").strip()
            if not city == "2":
                print("They are not ready.")
                break

            print("You chose Kostences. It takes 4 hours by car. So you can choose a place to start your travel:\n")

            print("1. -> Ovidius Square")
            print("2. -> Constanta Museum of History and Archaeology\n")

            place = input("Your choice for start place? -> (): \n ").strip()
            if not place == "":
                print("Your choice is \n")
                print(" \n")
            else:
                print("They are not ready.")
                break

            second_place = input("Your choice for start place? -> (): \n ").strip()
            if not second_place == "":
                print("Your choice is \n")
                print(" \n")
            else:
                print("They are not ready.")
                break


























            print("1. -> Bulgaria")
            print("2. -> Romania")
            print("3. -> Serbia")
            print("4. -> Greece")
            print("5. -> Croatia")
            print("6. -> Albania")
            print("7. -> Slovenia")
            print("8. -> Montenegro")
            print("9. -> Makedonia")
            print("10. -> Hungary")
            print("11. -> Bosna and Herzegovina\n")

            print("\nYour choice is Balkans. Please choose a country:\n ")
            country = input("Your choice for country? -> 1-11(3):\n ").strip()
            if not country == "3":
                print("They are not ready.")

            print("Your choice is Serbia. Please choose a city:\n ")



            print("8. -> ")
            print("9. -> \n")
            print("5. -> ")
            print("6. -> ")
            print("7. -> ")
            print("8. -> ")
            print("9. -> ")


            print("8. -> ")
            print("9. -> \n")
            print("5. -> ")
            print("6. -> ")
            print("7. -> ")
            print("8. -> ")
            print("9. -> ")

            city = input("Your choice for city? -> 1-3(1): \n ").strip()
            if not city == "1":
                print("They are not ready.")
                break

            print("8. -> ")
            print("9. -> \n")
            print("5. -> ")
            print("6. -> ")
            print("7. -> ")
            print("8. -> ")
            print("9. -> ")
Travel()
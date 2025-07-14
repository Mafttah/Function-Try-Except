while True:
    print("Europe -> 1")
    print("Asia -> 2")
    print("South America -> 3")
    secim = input("Which continent would you like to go to? -> 1,2,3:\n ").strip()

    if not secim == "1":
        print("They are not ready.")
        break

    print("\nWhich part of Europe would you like to go?\n ")
    print("1. East Europe (Russia, Ukranie, Poland, Slovakia, Lithuania, Latvia, Estonia, Moldova)")
    print("2. West Europe (England, Scotland, Wales, Ireland,Northern Ireland, France, Belgium, Netherland, Germany, Luxemburg)")
    print("3. Latin Countries (Spain, Portugal, Italy")
    print("4. Scandinavian Countries (Norway, Sweden, Fınland)")
    print("5. Middle Europe Czechia, Austria, Slovenia)")
    print("6. Balkans (Greece, Bulgaria, Romania, Montenegro, Makedonia, Serbia, Albania, Croatia, Hungary, Slovenia, Bosnia and Herzegovina)")
    part = input("What is your choice for part of Europe? -> 1,2,3,4,5,6:\n ").strip()

    if not part == "1":
        print("They are not ready.")
        break

    print("\nYour choice is East Europe. Please choose a country:\n ")
    print("1. Moldova")
    print("2. Ukraine")
    print("3. Poland")
    print("4. Slovakia")
    print("5. Lithuania")
    print("6. Latvia")
    print("7. Estonia")
    print("8. Russia")
    print("9. Belarus")
    country = input("Your choice for country? -> 1-9:\n ").strip()

    if not country == "1":
        print("They are not ready.")
        break

    print("Your choice is Moldova. Please choose a city:\n ")
    print("1. Kisinev")
    print("2. Tiraspol")
    print("3. Comrat")
    city = input("Your choice for city? -> 1,2,3:(1)\n ").strip()

    if not city == "1":
        print("They are not ready.")
        break

    print("You chose Kisinev. So you can choose a place to start your travel:\n ")
    print("1. Cathedral Park")
    print("2. Triumph Arc")
    print("3. Stefan Cel Mare Central Park")
    print("4. Stefan cel Mare si Sfant Boulevard")
    print("5. Valea Morilor Park")
    print("6. Mustafa Kemal Atatürk Library")
    print("7. Strada Lenin Street")
    print("8. Central Park")
    place = input("Where do you want to start? -> 1-8(4):\n ").strip()

    if place == "4":
        print("Your choice is Stefan cel Mare si Sfant Boulevard.\n")
    else:
        print("They are not ready.")
        break

    second_place = input("After travelling the Boulevard, where do you want to go next? -> 1-4 6-8 (2): ").strip()
    if second_place == "2":
        print("Your choice is Triumph Arc.\n")
        print("When you finish travelling the Boulevard, just walk straight to see it.\n")
        print("The copper from cannons captured by Russian forces from the Ottoman Empire was melted down. The bell, (also known as the Clopote-Velican bell,) was originally designed for use in the cathedral's bell tower, but because it was so large, it was decided to use it on the Triumphal Arch.\n")
    else:
        print("They are not ready.")
        break

    third_place = input("After travelling the Arc, where do you want to go next? -> 1,3,4,6,8 (1): ").strip()
    if third_place == "1":
        print("Your choice is Cathedral Park.\n")
        print("When you arrive Cathedral Park, you will see the Cathedral of the Nativity located in the center of the park." "--The main cathedral of the Moldovan Orthodox Church. Built in the 1830s by order of the governor of New Russia, Prince Mikhail Semyonovich Vorontsov, the cathedral was designed by the renowned Russian architect Abram Melnikov.--\n")
        print("Opening Hours: Weekdays 08:00-16:00 | Weekends 08:00-20:00")
        print("Entry: Free\n")
    else:
        print("They are not ready.")
        break

    forth_place = input("After Cathedral Park, where next? -> 3,4,6,8 (3): ").strip()
    if forth_place == "3":
        print("Your choice is Stefan Cel Mare Central Park.\n")
        print("Moldova's oldest and most impressive park is the 7-hectare Stefan Cel Mare Central Park, which is very popular with locals, especially during the summer months. Children's playgrounds make the park a particularly good choice for families. In other parts of the park, you can see busts of Moldovan and Romanian writers and political figures")    
    else:
        print("They are not ready.")
        break

    fifth_place = input("Where to next? -> 5,6,8 (5): ").strip()
    if fifth_place == "5":
        print("Your choice is Valea Morilor Park.\n")
        print("Newlyweds often come here to take photos. But what makes the park special is that archaeological excavations have revealed that mammoths once lived here. Valea Morilor Park's most striking feature is the Pavilion and, immediately in front of it, the cascade of steps with flowing water, reminiscent of Pamukkale. The steps begin in front of the Pavilion and lead down to Komsomolsky Lake.")
    else:
        print("They are not ready.")
        break
    city = input("Your choice for city? -> ,2,3:(3)\n ").strip()

    if not city == "3":
        print("They are not ready.")
        break

    sixth_place = input("Where to next? -> 7,8 (7): ").strip()
    if sixth_place == "7":
        print("Your choice is Comrat and you will go firstly Strada Lenin Street.\n")
        print("Note1: Moldova is said to consist of three distinct regions. Gagauzia, or Gagauzia, as it is called, is one of Moldova's three regions. Following Moldova's independence in 1994, the Moldovan government granted Gagauzia special status.\n")
        print("Note2: It takes two hours to get to Comrat from Chişinău, or vice versa.\n")
        print("It's located in Comrat!, the capital of Gagauvia. Strada Lenin 197 is Comrat's largest street. You can see the government buildings here.")
    else:
        print("They are not ready.")
        break

    seventh_place = input("Where to next? -> 6,8 (6): ").strip()
    if seventh_place == "6":
        print("Your choice is Mustafa Kemal Atatürk Library.\n")
        print("The library is located on Strada Lenin Street Street and There is a bust of Atatürk in the garden of the library.")
    else:
        print("They are not ready.")
        break

    eighth_place = input("Where to next? -> 8: ").strip()
    if eighth_place == "8":
        print("Your choice is Central Park in Comrat.\n")
        print("Right in the center of Comrat is Parcul Central. The yellow Orthodox church of Sankt Ioan Botezatorul is a standout. The park square also boasts numerous restaurants.\n")
        print("After visiting this place. In addition to these attractions:\n ")
        print("1. -> National History Museum of Moldova\n")
        print(f"Opening Hourse: Close on Mondays but other days it is open between 10.00 - 18.00\n"
                "Entry fee: Adults -> 50 MDL, Pensioners, students -> 20 MDL, child -> 10 MDL")
        print("1. -> Pushkin Museum\n")
        print(f"Opening Hourse: Close on Mondays but other days it is open between 10.00 - 19.00\n"
                "Entry fee: Adults -> 1000 MDL, 7-18 student -> 800 MDL\n")
    else:
        print("They are not ready.")
        break

    print("2. Tiraspol")
    print("4. Balti")
    print("5. Soroca")
    city = input("Your choice for city? -> 2-4-5(2):\n ").strip()

    if not city == "2":
        print("They are not ready.")
        break
    print("You chose Tiriaspol. So you can choose a place to start your travel:\n ")

    print("1. -> Noul Neamt Monastry")
    print("2. -> 25th October Street")
    place = input("Where do you want to start? -> 1-2:\n ").strip()

    if place == "1":
        print("Your choice is Noul Neamt Monastry.\n")
        print("Noul Neamt Monastery, one of Tiraspol's most impressive structures with its 70-meter main tower, is 7 kilometers south of the city. Situated in the countryside, you can climb up to the church tower for a panoramic bird's-eye view.\n")
    else:
        print("They are not ready.")
        break

    second_place = input("Where to next? -> 2: ").strip()
    if second_place == "2":
        print("Your choice is 25th October Street.\n")
        print("25 October Street, one of the city's symbolic stops, is also its busiest. Surrounded by numerous parks, this area is also very close to the city's university and home to the Cultural Park. The street, which also houses an amusement park, is also home to numerous sculptures.")
    else:
        print("They are not ready.")
        break

    print("You've finished visiting Chisinau. You can choose the next city.\n")

    print("4. Balti")
    print("5. Soroca")
    city = input("Your choice for city? -> 4-5:\n ").strip()

    if not city == "4":
        print("They are not ready.")
        break
    print("You chose . So you can choose a place to start your travel:\n ")

    print("1. -> St Constantin and Helena Cathedral")
    print("2. -> St. Nicolae Cathedral Balti")
    place = input("Where do you want to start? -> 1-2:\n ").strip()

    if place == "1":
        print("Your choice is St Constantin and Helena Cathedral.\n")

        print("Construction began in 1924 and is a neo-Byzantine style. The cathedral has remained virtually untouched since its construction and remains in its pristine condition. The Cathedral of Saints Constantine and Helena captivates visitors with its vibrant blue and white hue.\n")
    else:
        print("They are not ready.")

        second_place = input("After travelling the St Constantin and Helena Cathedral, where do you want to go next? -> 2: ").strip()
    if second_place == "2":
        print("Your choice is St. Nicolae Cathedral Balti.\n")
        print("The church dates back to the 1700s. The only damage was the collapse of the bell tower in 1962, but it was rebuilt in 1995.\n")
    else:
        print("They are not ready.")
        break

    print("5. Soroca")
    city = input("Your choice for city? -> 5:\n ").strip()

    if not city == "5":
        print("They are not ready.")
        break
    print("You chose Soroca. So you can choose a place to start your travel:\n ")

    print("1. -> Soroco Fortress")
    place = input("Where do you want to start? -> 1:\n ").strip()

    if place == "1":
        print("Your choice is Soroco Fortress.\n")
        print("The city has its origin in the medieval Genoese trade post of Olchionia, or Alchona. It is known for its well-preserved stronghold, established by the Moldavian Prince Stephen the Great in 1499. The original wooden fort, which defended a ford over the Dniester (Romanian: Nistru), was an important link in the chain of fortifications which comprised four forts (e.g. Akkerman and Khotin) on the Dniester, two forts on the Danube and three forts on the north border of medieval Moldova. Between 1543 and 1546 under the rule of Petru Rareş, the fortress was rebuilt in stone as a perfect circle with five bastions situated at equal distances.")
    else:
        print("They are not ready.")

    print("2. Ukraine")
    print("3. Poland")
    print("4. Slovakia")
    print("5. Lithuania")
    print("6. Latvia")
    print("7. Estonia")
    print("8. Russia")
    print("9. Belarus")
    country = input("Your choice for country? -> 2-9:\n ").strip()

    if not country == "2":
        print("They are not ready.")
        break

    print("Your choice is Ukraine. Please choose a city:\n ")
    print("1. Kisinev")
    print("2. Tiraspol")
    print("3. Comrat")
    city = input("Your choice for city? -> 1,2,3:(1)\n ").strip()

    if not city == "1":
        print("They are not ready.")
        break


print("5. ")
print("6. ")
print("7. ")
print("8. ")






def Travel():
    while True:
        print(f"Continent Selection\n")
        print(f"1. Europe\n2. Asia\n3. America, 0. Exit\n")
        secim = input("Select a continent: ").strip()

        if secim == "0":
            print("Exiting program.")
            break
        elif secim == "1":
            print("Selected: Europe\n")
            print("Regions in Europe\n")
            print(f"1. East Europe (Russia, Ukraine, Poland, etc.), 2. West Europe (England, France, Germany, etc.), 3. Latin (Spain, Portugal, Italy), 4. Scandinavian (Norway, Sweden, Finland), 5. Central Europe (Austria, Hungary, Czechia, etc.), 6. Balkans (Greece, Romania, Serbia, etc.)\n")
            input("Select a region: ")

        elif secim == "2":
            print("Selected: Asia\n")
            print(f"Regions in Asia\n")
            print(f"1. Middle East\n2. South Asia\n3. Southeast Asia\n4. East Asia\n5. Central Asia\n6. North Asia\n7. Western Asia\n8. Southern Asia\n9. Eastern Asia\n10. South-Eastern Asia\n\n")
            input("Select a region: ")

        elif secim == "3":
            print("Selected: America\n")
            print(f"Regions in America\n")
            print(f"1. North America\n2. Central America\n3. South America\n4. Caribbean    \n5. Latin America\n6. Andean Region\n7. Amazon Basin\n8. Southern Cone\n9. Great Plains\n10. Gulf Coast\n11. Pacific Northwest\n12. Atlantic Coast\n13. Rocky Mountains\n14. Appalachian Mountains\n15. Great Lakes Region\n16. New England Region\n17. Midwestern Region\n18. Southwestern Region\n19. Southeastern Region")
            input("Select a region: ")
        else:
            print("Invalid selection. Try again.")
            break

    while True:
        part = input("Select a region: ")
        print(f"Selected: {part}")
        break
    print("\nYour choice is East Europe. Please choose a country:\n ")
    print(f"1. Moldova", "2. Ukraine", "3. Poland", "4. Estonia", "5. Lithuania", "6. Russia", "7. Belarus", "8. Latvia \n")
    country = input("Your choice for country? -> 1-8(1):\n ").strip()
    if not country == "1":
        print("They are not ready.")

    print("Your choice is Moldova. Please choose a city:\n")
    print(f"1. Kisinev and Comrat", "2. Tiraspol", "3. Balti", "4. Soroca")
    city = input("Your choice for city? -> 1,2,3,4:(1)\n ").strip()
    if city == "1":
        print("You have selected Kisinev and Comrat. So you can choose a place to start your travel:\n ")
    else:
        print("They are not ready.")

    while True:
        print(f"1. Cathedral Park", "2. Triumph Arc", "3. Stefan Cel Mare Central Park", "4. Stefan cel Mare si Sfant Boulevard", "5. Valea Morilor Park", "6. Mustafa Kemal Atatürk Library", "7. Strada Lenin Street", "8. Central Park")
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

        sixth_place = input("Where to next? -> 7,8 (7): ").strip()
        if sixth_place == "7":
            print("Your choice is Strada Lenin Street.\n")
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

    while True:
        print("You've finished visiting Chisinau. You can choose the next city.\n")
        print("1. -> Tiraspol", "2. -> Balti", "3. -> Soroca\n")
        next_city = input("Where to next? -> 1-3(1):\n ").strip()
        if next_city == "1":
            print("Your choice is Tiraspol.")
        else:
            print("They are not ready.")
            break

    while True:
        print("You chose Tiraspol. So you can choose a place to start your travel:\n ")
        print("1. -> Noul Neamt Monastry", "2. -> 25th October Street")
        print("You can choose a place to start your travel:\n ")
        place = input("Where do you want to start? -> 1-2(1):\n ").strip()
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
        print("You have finished travelling Tiraspol. You can choose other city.\n")
        print("1. -> Balti", "2. -> Soroca")
        break
    while True:
        next_city = input("Where to next? -> 1-2(1):\n ").strip()
        if next_city == "1":
            print("Your choice is Balti.")
        else:
            print("Invalid choice. Please select a valid city.")
            continue
        print("You chose Balti. So you can choose a place to start your travel:\n ")

        print(f"1. -> St Constantin and Helena Cathedral", "2. -> St. Nicolae Cathedral Balti")
        place = input("Where do you want to start? -> 1-2(1):\n ").strip()
        if place == "1":
            print("Your choice is St Constantin and Helena Cathedral.\n")

            print("Construction began in 1924 and is a neo-Byzantine style. The cathedral has remained virtually untouched since its construction and remains in its pristine condition. The Cathedral of Saints Constantine and Helena captivates visitors with its vibrant blue and white hue.\n")
        else:
            print("They are not ready.")
            break

        second_place = input("After travelling the St Constantin and Helena Cathedral, where do you want to go next? -> 2: ").strip()
        if second_place == "2":
            print(f"Your choice is St. Nicolae Cathedral Balti.\n", "The church dates back to the 1700s. The only damage was the collapse of the bell tower in 1962, but it was rebuilt in 1995.\n")
        else:
            print("They are not ready.")

        print("You have finished travelling Balti. You can choose other city.\n")
        break
    while True:
        print("5. Soroca")
        city = input("Your choice for city? -> 5:\n ").strip()

        if not city == "5":
            print("They are not ready.")
            break

        print("You chose Soroca. So you can choose a place to start your travel:\n ")

        print("1. -> Soroco Fortress")
        place = input("Where do you want to start? -> 1:\n ").strip()

        if place == "1":
            print(f"Your choice is Soroco Fortress.\n", "The city has its origin in the medieval Genoese trade post of Olchionia, or Alchona. It is known for its well-preserved stronghold, established by the Moldavian Prince Stephen the Great in 1499. The original wooden fort, which defended a ford over the Dniester (Romanian: Nistru), was an important link in the chain of fortifications which comprised four forts (e.g. Akkerman and Khotin) on the Dniester, two forts on the Danube and three forts on the north border of medieval Moldova. Between 1543 and 1546 under the rule of Petru Rareş, the fortress was rebuilt in stone as a perfect circle with five bastions situated at equal distances.")
        else:
            print("They are not ready.")
            break

    while True:
        print("You have finished travelling Moldova. You can choose other country.\n")
        print("2. -> Ukraine", "3. -> Russia", "4. -> Estonia", "5. -> Lithuania", "6. -> Belarus", "7. -> Poland", "8. -> Latvia\n")

        country = input("Where to next? -> 2-8(2):\n ").strip() 
        if not country == "2":
            print("They are not ready.")
            print("Your choice is Ukraine. Please choose a city:\n ")
            print(f"1. -> Odessa", "2. -> Lviv", "3. -> Lutsk", "4. -> Kharkiv", "5. -> Kiev", "6. -> Zaporizhya", "7. -> Donetsk")
            city = input("Your choice for city? -> 1-8:(1)\n ").strip()

            if not city == "1":
                print("They are not ready.")
                break

            print("You chose Odessa. So you can choose a place to start your travel:\n")

            print(f"1. -> Shevchenko Park", "2. -> Potemkin Stairs", "3. -> Primorskyi Boulevard", "4. -> Vorontsov Palace", "5. -> Monument to Catherine II", "6. -> Deribasovskaya Street", "7. -> City Garden", "8. -> Theater square")
            place = input("Where do you want to start? -> 1-8(1):\n ").strip()
            if place == "1":
                print("Your choice is Shevchenko Park.\n")
                print("Shevchenko Park, opened in 1875, is a bit outside the city center, but it's still a must-see. Located near Lanzheron Park, the park's entrance features a Shevchenko monument and a monument to Tsar Alexander II, restored since the Soviet era.\n")
            else:
                print("They are not ready.")
                break

            second_place = input("After travelling the Shevchenko Park, where do you want to go next? -> 2-8(8): ").strip()
            if second_place == "8":
                print("Your choice is Theater square\n")
                print("After Deribasovskaya and Primorsky Squares, it's another important square in Odessa. When you're looking for information about Odessa, the Opera House is one of the images that will undoubtedly come to mind. With its magnificent architecture, magnificent structure, and the cultural and artistic events it hosts, the Opera House is one of the city's most important structures and is just one of the architectural wonders of Teatralnaya Square.\n")
            else:
                print("They are not ready.")
                break

            third_place = input("After travelling the Theater square, where do you want to go next? -> 2-7(6): ").strip()
        if third_place == "6":
            print("Your choice is Deribasovskaya Street\n")
            print("It's both the city's main street and Odessa's most touristy spot. Because it's closed to traffic, it's quite popular with tourists. You'll find some of the city's leading restaurants and cafes along the street. This approximately 1-kilometer-long street also offers a wide variety of shopping options.\n")
        else:
            print("They are not ready.")
            

            forth_place = input("After , where next? -> 2-7(7): ").strip()
            if forth_place == "7":
                print("Your choice is City Garden.\n")
                print("It's the city's oldest park and was established on a private property by José de Ribas's brother in 1803. Opening onto Deribasovskaya Street, the park is a short walk from the city center. The City Garden also contains several monuments honoring Odessa's cultural figures.\n")    
            else:
                print("They are not ready.")
            

            fifth_place = input("Where to next? -> 2-6(5): ").strip()
            if fifth_place == "5":
                print("Your choice is Monument to Catherine II\n")
                print("Following Katerynyns'ka Street from the upper level of the Potemkin Stairs, you'll encounter the Catherine II Monument, a place where you can find information about Odessa's past. In addition to the statue of Catherine II, who made the decision to build a port and city in 1794, there are also statues of Catherine's advisors, Count Grigory Potemkin, military officer José de Ribas, Platon Zubov, and finally, the Flemish engineer François Sainte de Wollant. The monument was erected in 1900 and removed in the 1920s during the Soviet era. It was relocated and restored in 2007, taking its current form.\n")
            else:
                print("They are not ready.")


            sixth_place = input("Where to next? -> 2-6(3): ").strip()
            if sixth_place == "3":
                print("Your choice is Primorskyi Boulevard\n")
                print("Primorskyi Boulevard is like an open-air museum in Odessa. Its architecture offers a visual feast, and it also hosts numerous historical and tourist attractions. As the beating heart of the city, it is one of its most popular attractions. Adorned with chestnut, plane, and linden trees, it is located right next to Istanbul Park.\n")
            else:
                print("They are not ready.")


            seventh_place = input("Where to next? -> 2-6(2): ").strip()
            if seventh_place == "2":
                print("Your choice is Potemkin Stairs.\n")
                print("It is one of the city's most well-known and popular tourist attractions. Built in the early 1840s, the granite staircase was commissioned by Prince Vorontsov as a gift to his wife. It has a total of 192 steps, 142 meters long and 27 meters above sea level. The stairs are much wider at the bottom (21.7 meters) than at the top (12.5 meters). This was intentionally done to create a false perspective and make the stairs appear larger when viewed from below. Built as the official sea entrance to Odessa, the Potemkin Stairs are used as seating for open-air music concerts and film screenings.\n")
            else:
                print("They are not ready.")


            eighth_place = input("Where to next? -> 4: ").strip()
            if eighth_place == "4":
                print("Your choice is Vorontsov Palace.\n")
                print("One of the most important historical buildings in Odessa, the Vorontsov Palace was built in 1827, a blend of architectural styles. Built on the site of a Turkish fortress, it was the residence of the Governor-General of the Russian statesman and military leader Mikhail Vorontsov. Today, the palace serves as an art center and a center for youth cultural activities. Located at the western end of Primorsky Boulevard, a short walk from the Orange Monument, it was commissioned by Prince Mikhail Semyonovich Vorontsov and commissioned by Sardinian architect Francesco Boffo.\n")

            print("You've finished visiting Odessa. You can choose the next city.\n")

            print("2. -> Lviv")
            print("3. -> Lutsk")
            print("5. -> Kharkiv")
            print("6. -> Kiev")
            print("7. -> Zaporizhya")
            print("8. -> Donetsk")
            city = input("Your choice for city? -> 2-8:(7)\n ").strip()
Travel()


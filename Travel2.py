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
            print(f"Regions in Europe: \n", "1. East Europe (Russia, Ukraine, Poland, etc.), 2. West Europe (England, France, Germany, etc.), 3. Latin (Spain, Portugal, Italy), 4. Scandinavian (Norway, Sweden, Finland), 5. Central Europe (Austria, Hungary, Czechia, etc.), 6. Balkans (Greece, Romania, Serbia, etc.)\n")
            input("Select a region: ")

        elif secim == "2":
            print("Selected: Asia\n")
            print(f"Regions in Asia: \n", "1. Middle East\n2. South Asia\n3. Southeast Asia\n4. East Asia\n5. Central Asia\n6. North Asia\n7. Western Asia\n8. Southern Asia\n9. Eastern Asia\n10. South-Eastern Asia\n\n")
            input("Select a region: ")

        elif secim == "3":
            print("Selected: America\n")
            print(f"Regions in America: \n")
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
            break

    while True:
        print("Your choice is Ukraine. Please choose a city:\n ")
        print(f"1. -> Odessa", "2. -> Lviv", "3. -> Lutsk", "4. -> Kharkiv", "5. -> Kiev", "6. -> Zaporizhya", "7. -> Donetsk")
        city = input("Your choice for city? -> 1-8:(1)\n ").strip()

        if not city == "1":
            print("They are not ready.")
            break

        print("You chose Odessa. So you can choose a place to start your travel:\n")

    while True:
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
            break

        forth_place = input("After , where next? -> 2-7(7): ").strip()
        if forth_place == "7":
            print("Your choice is City Garden.\n")
            print("It's the city's oldest park and was established on a private property by José de Ribas's brother in 1803. Opening onto Deribasovskaya Street, the park is a short walk from the city center. The City Garden also contains several monuments honoring Odessa's cultural figures.\n")    
        else:
            print("They are not ready.")
            break

        fifth_place = input("Where to next? -> 2-6(5): ").strip()
        if fifth_place == "5":
            print("Your choice is Monument to Catherine II\n")
            print("Following Katerynyns'ka Street from the upper level of the Potemkin Stairs, you'll encounter the Catherine II Monument, a place where you can find information about Odessa's past. In addition to the statue of Catherine II, who made the decision to build a port and city in 1794, there are also statues of Catherine's advisors, Count Grigory Potemkin, military officer José de Ribas, Platon Zubov, and finally, the Flemish engineer François Sainte de Wollant. The monument was erected in 1900 and removed in the 1920s during the Soviet era. It was relocated and restored in 2007, taking its current form.\n")
        else:
            print("They are not ready.")
            break

        sixth_place = input("Where to next? -> 2-6(3): ").strip()
        if sixth_place == "3":
            print("Your choice is Primorskyi Boulevard\n")
            print("Primorskyi Boulevard is like an open-air museum in Odessa. Its architecture offers a visual feast, and it also hosts numerous historical and tourist attractions. As the beating heart of the city, it is one of its most popular attractions. Adorned with chestnut, plane, and linden trees, it is located right next to Istanbul Park.\n")
        else:
            print("They are not ready.")
            break

        seventh_place = input("Where to next? -> 2-6(2): ").strip()
        if seventh_place == "2":
            print("Your choice is Potemkin Stairs.\n")
            print("It is one of the city's most well-known and popular tourist attractions. Built in the early 1840s, the granite staircase was commissioned by Prince Vorontsov as a gift to his wife. It has a total of 192 steps, 142 meters long and 27 meters above sea level. The stairs are much wider at the bottom (21.7 meters) than at the top (12.5 meters). This was intentionally done to create a false perspective and make the stairs appear larger when viewed from below. Built as the official sea entrance to Odessa, the Potemkin Stairs are used as seating for open-air music concerts and film screenings.\n")
        else:
            print("They are not ready.")
            break

        eighth_place = input("Where to next? -> 4: ").strip()
        if eighth_place == "4":
            print("Your choice is Vorontsov Palace.\n")
            print("One of the most important historical buildings in Odessa, the Vorontsov Palace was built in 1827, a blend of architectural styles. Built on the site of a Turkish fortress, it was the residence of the Governor-General of the Russian statesman and military leader Mikhail Vorontsov. Today, the palace serves as an art center and a center for youth cultural activities. Located at the western end of Primorsky Boulevard, a short walk from the Orange Monument, it was commissioned by Prince Mikhail Semyonovich Vorontsov and commissioned by Sardinian architect Francesco Boffo.\n")
            break

        print("You've finished visiting Odessa. You can choose the next city.\n")
    
    while True:
        print(f"2. -> Lviv", "3. -> Lutsk", "5. -> Kharkiv", "6. -> Kiev", "7. -> Zaporizhya", "8. -> Donetsk")
        city = input("Your choice for city? -> 2-8:(7)\n ").strip()
        if not city == "7":
            print("They are not ready.")
            break

        print("You chose Zaporijya. It takes 6 hours by car. So you can choose a place to start your travel:\n")

    while True:
        print("1. -> St. Andrew's Cathedral")
        print("2. -> Zaporizhia Sich")
        print("3. -> Preobrazhenskiy Bridge")
        place = input("Where do you want to start? -> 1-3(2):\n ").strip()
        if place == "2":
            print("Your choice is Zaporizhia Sich.\n")

            print("The Zaporizhian Sich, a group of military settlements that existed between the 16th and 18th centuries, was flooded by the construction of dams during the Soviet era. Now, in addition to its historical significance for Ukraine, it is also home to a tradition initiated by newlyweds before the ceremony.\n")
        else:
            print("They are not ready.")
            break

        second_place = input("After travelling the Zaporizhia Sich, where do you want to go next? -> 1-3(3): ").strip()
        if second_place == "2":
            print("Your choice is Preobrazhenskiy Bridge\n")
            print("The 550-meter-long bridge, built in 1952, was considered impossible by some. Therefore, the Preobrazhensky Bridge, considered an architectural masterpiece, consists of four arches. The bridge has two floors, the upper floor for the railway line, and the lower floor for pedestrians and private trucks.\n")
        else:
            print("They are not ready.")
            break    

        third_place_place = input("After , where next? -> 1(1): ").strip()
        if third_place_place == "1":
            print("Your choice is St. Andrew's Cathedral.\n")
            print("Built in 2001 with the help of donations, St. Andrew's Cathedral is a blend of Baroque and modern architecture. The cathedral, the city's most visited place of worship, is also considered a monument.\n")    
        else:
            print("They are not ready.")
            break

        print("You've finished visiting Zaporijya. You can choose the next city.\n")
    
    while True:
        print(f"2. -> Lviv", "3. -> Lutsk", "5. -> Kharkiv", "6. -> Kiev", "8. -> Donetsk")
        city = input("Your choice for city? -> 2-8:(8)\n ").strip()
        if not city == "8":
            print("They are not ready.")
            break

        print("You chose Donetsk. It takes 4 hours by car. So you can choose a place to start your travel:\n")
    
    while True:
        print(f"1. -> Pushkina Boulevard", "2. -> Svyato Preobrazhensky Cathedral", "3. -> Shcherbakov Park of Culture and Leisure")
        place = input("Where do you want to start? -> 1-3(3):\n ").strip()

        if place == "3":
            print("Your choice is Shcherbakov Park of Culture and Leisure.\n")
            print("You can visit Donetsk Cultural Park, considered the heart of the city. This park, one of the city's most popular spots, offers both relaxation and a pleasant time. The park boasts numerous facilities, including exclusive restaurants, cycling trails, a summer theater, a dolphin park, and a checkerboard area. It covers an area of 62 hectares.\n")
        else:
            print("They are not ready.")
            break

        second_place = input("After travelling the Shcherbakov Park of Culture and Leisure, where do you want to go next? -> 1-2(1): ").strip()
        if second_place == "1":
            print("Your choice is Pushkina Boulevard\n")
            print("It's one of the city's most interesting spots. After a pleasant stroll along Pushkin Boulevard, lined with cafes and restaurants, you can shop in the surrounding stores.\n")
        else:
            print("They are not ready.")
            break    

        third_place_place = input("After Pushkina Boulevard, where next? -> 2(2): ").strip()
        if third_place_place == "2":
            print("Your choice is Svyato Preobrazhensky Cathedral\n")
            print("Dating back to 1883, the cathedral is one of the most important structures that offers a firsthand glimpse into the city's historical and religious architecture. Affiliated with the Orthodox Church, the Svyato-Preobrazhensky Cathedral is the largest religious structure you'll ever see. It is also the largest structure in Ukraine.\n")    
        else:
            print("They are not ready.")
            break

        print("You've finished visiting Zaporijya. You can choose the next city.\n")

        print(f"2. -> Lviv", "3. -> Lutsk", "4. -> Odesa", "5. -> Kharkiv", "6. -> Kiev")
        city = input("Your choice for city? -> 2-6:(5)\n ").strip()

        if not city == "5":
            print("They are not ready.")
            break

        print("You chose Kharkiv. It takes 5 hours and 30 minutes by car. So you can choose a place to start your travel:\n")

    while True:    
        print(f"1. -> Freedom Square", "2. -> Pokrovsky Monastery - Svyato-Pokrovsky boy monastry", "3. -> Shevchenko City Garden", "4. -> Uspensky Cathedral - Assumption Cathedral", "5. -> Annunciation Cathedral - Blahovishchens Kafedral")
        place = input("Where do you want to start? -> 1-5(4):\n ").strip()

        if place == "4 - Uspensky Cathedral - Assumption Cathedral":
            print("Kharkiv's oldest Orthodox cathedral, the Cathedral, is located in the Old Town district. It served as the city's main center of worship until the Annunciation Cathedral was built in 1901. Belonging to the Orthodox Church, the building reflects neoclassical style.\n")
        else:
            print("They are not ready.")
            break

        second_place = input("After travelling the Assumption Cathedral, where do you want to go next? -> 1-5(2): ").strip()
        if second_place == "2":
            print("Your choice is Pokrovsky Monastery - Svyato-Pokrovsky boy monastry\n")
            print("Located in Kharkiv's city center, the monastery is the city's oldest structure, built in 1689. The structure, which has survived to this day, was designed in the style of traditional Ukrainian domed churches. Its architecture makes it one of the seven wonders of Kharkiv. The monastery was damaged during World War II and restored in the early 1990s.\n")
        else:
            print("They are not ready.")
            break            

        third_place_place = input("After Svyato-Pokrovsky boy monastry, where next? -> 1-5(5): ").strip()
        if third_place_place == "5 - Annunciation Cathedral - Blahovishchens Kafedral":
            print("Located in the historic city center, the Annunciation Cathedral is built in the Byzantine architectural style. The first Annunciation Cathedral was built in the mid-17th century, but this wooden structure was completely destroyed in a major fire that ravaged the city in 1738. Fifty years later, a new cathedral was built on the same site, but this too proved inadequate. The city's need for a large and magnificent cathedral led to the completion of the Annunciation Cathedral in 1888, which has survived to this day, and took approximately 30 years to complete. For a time, the Annunciation Cathedral was closed to worship, and today it is affiliated with the Orthodox Church and is Kharkiv's most important center of worship.\n")    
        else:
            print("They are not ready.")
            break

        forth_place = input("After Annunciation Cathedral - Blahovishchens Kafedral, where next? -> 1-4(1): ").strip()
        if forth_place == "1":
            print("Your choice is Freedom Square\n") 
            print("Visiting Kharkiv: It is the eighth largest square in Europe and the fifteenth largest in the world. Located at the heart of the city, it was built in the early 20th century when Kharkiv was the capital of the Ukrainian Soviet Socialist Republic. Freedom Square has been the city's center since its construction. Today, official holidays, festivals, and concerts are held here.\n")    
        else:
            print("They are not ready.")
            break

        fifth_place = input("Where to next? -> 3-4(3): ").strip()
        if fifth_place == "3":
            print("Your choice is Shevchenko City Garden\n")
            print("Magnificent Shevchenko Park is Kharkiv's oldest and largest park. It contains beautiful green spaces, important monuments, playgrounds, and the Kharkiv Zoo. Built between 1804 and 1805 by Vasily Karazin, founder of Kharkiv University, the park hosts a natural insect exhibition every summer.\n")
        else:
            print("They are not ready.")
            break

        print("You've finished visiting Kharkiv. You can choose the next city.\n")

        print("2. -> Lviv")
        print("3. -> Lutsk")
        print("6. -> Kiev")
        city = input("Your choice for city? -> 2-6:(6)\n ").strip()

        if not city == "6":
            print("They are not ready.")
            break
        
        print("You chose Kiev. It takes 6 hours and 30 minutes by car. So you can choose a place to start your travel:\n")
    
    while True:
        print(f"1. -> Taras Shevchenko Park", "2. -> Saint Sophia's Cathedral", "3. -> Khreshchatyk", "4. -> Pechersk Lavra - Monastery of the Caves", "5. -> Independence Square - Maidan Nezaleshnosti", "6. -> Andrevski Spusk", "7. -> Mariyinsky Palace and Park", "8. -> St. Andrew's Church", "9. -> Mother Motherland\n")

        place = input("Where do you want to start? -> 1-9(9):\n ").strip()
        if place == "9":
            print("Your choice is Mother Motherland\n")
            print("It's a statue of a woman, as large as any you'll see in many parts of Kiev, holding a sword, symbolizing war. Considered one of the most awe-inspiring statues in Kiev, Mother Motherland stands atop a hill overlooking the Dnieper River. Its height of 102 meters alone makes it one of the most impressive statues in the world. It's also the largest female statue in the world, but it would be unfair to single out it for its sheer size. Its striking gold color makes it also known as the Rodina Mat, or Motherland Statue. Built to commemorate World War II, the woman in the Rodina Mat statue, holding a sword, represents the fight against the enemy. The Museum of the Great Patriotic War, located beneath the monument, sheds light on the history of Kiev.\n")
        else:
            print("They are not ready.")
            break

        second_place = input("Where to next? -> 1-8(4): ").strip()
        if second_place == "4":
            print("Your choice is Pechersk Lavra\n")
            print("It is the center of Christianity in Eastern Europe and a very complex structure. Built in 1051 by Prince Yaroslav I as one of the first monasteries, while Kiev was still part of Russia, the Monastery of the Caves encompasses numerous churches, monasteries, and other structures. These caves are one of the features that make the Monastery of the Caves so special, having hosted nearly 50 million tourists from around the world to date. Beneath the structure are underground caves that can be explored with great curiosity by candlelight and a guide. Furthermore, the Pechersk Lavra holds great significance for the Orthodox world; Orthodox Christians visit here as pilgrims and for their religious observances. There are also special accommodations and prayer areas for pilgrims.\n")
        else:
            print("They are not ready.")
            break

        third_place = input("Where to next? -> 1-8(7): ").strip()
        if third_place == "7":
            print("Your choice is Mariyinsky Palace and Park\n")
            print("Dating back to the 1700s, the building was commissioned by Russian Empress Elizavata Petrovna. Today, it is used for official ceremonies by the President of Ukraine. Another important building for politicians is the Ukrainian Parliament Building, located right next to the palace. The building is constructed in the neoclassical architectural style. Mariinsky Palace served as headquarters during the war and as a school afterward. The palace, which once served the royal family, never survived the fires. After its forced demolition, Konstantin Mayevsky succeeded in rebuilding the palace using old drawings. The current palace park was also built after this period. You can also see the graves of famous figures and many monuments in the park. The palace, severely damaged during World War II, has been restored to its current appearance following restoration.\n")
        else:
            print("They are not ready.")
            break

        forth_place = input("Where to next? -> 1-8(1): ").strip()
        if forth_place == "1":
            print("Your choice is Taras Shevchenko Park\n")
            print("Taras Shevchenko Park boasts a botanical garden, cafe, restaurant, walking path, zoo, and dolphinarium. Dating back to 1805, the park is one of Kyiv's oldest historical and natural sites. Located next to the university, you'll also encounter many students who come to the park for a break, relaxation, and fun. Taras Shevchenko Park, a favorite spot for Kyiv residents, is also a place for exercise and walking. Speaking of which, if you'd like to sample Ukrainian local cuisine, the park's restaurant is also open. The famous park is also a popular venue for cultural events, protests, and demonstrations.\n")
        else:
            print("They are not ready.")
            break

        fifth_place = input("Where to next? -> 2-8(3): ").strip()
        if fifth_place == "3":
            print("Your choice is Khreshchatyk\n")
            print("It's Kiev's most popular and main street. Let's start with some of its basic features. Khreshchatyk Street is 1.2 km long, passing through the center of Independence Square and extending all the way to Bessarabska Square. It's lively day and night, right in the heart of the city. You'll find shopping malls, boutiques, shops, restaurants, and bars here.\n")
        else:
            print("They are not ready.")
            break

        sixth_place = input("Where to next? -> 2-8(5): ").strip()
        if sixth_place == "5":
            print("Your choice is Maidan Nezaleshnosti\n")
            print("Since the Ukrainian Independence Movement in 1990, it has been the center of numerous political demonstrations and protests, but the square's activities cannot be limited to these. It is also a place where many non-political activities take place. Kireshatik, the city's most popular street, runs through the heart of Independence Square. The square is divided into Kireshatik Street and the Monument and Globe areas. The Victory Column, located at the very center of Independence Square, is a symbol of Ukraine's independence and was erected in the square on the 10th anniversary of its independence. A statue of Berehynia, a woman adorned with rose branches, is placed atop the 61-meter-tall monument.\n")
        else:
            print("They are not ready.")
            break

        seventh_place = input("Where to next? -> 2-8(2): ").strip()
        if seventh_place == "2":
            print("Your choice is Saint Sophia’s Cathedral\n")
            print("It has been listed as a UNESCO World Heritage Site. Its history dates back to the 11th century. In fact, the cathedral's 1000th anniversary was celebrated in 2011. The fact that such an old structure has preserved its original appearance so well is truly awe-inspiring. The cathedral is so unique and intriguing that it was voted one of the Seven Wonders of Ukraine. For a bird's-eye view of the city, you can also climb the Bell Tower.\n")
        else:
            print("They are not ready.")
            break

        eighth_place = input("Where to next? -> 6-8(8): ").strip()
        if eighth_place == "8":
            print("Your choice is St. Andrew’s Church\n")
            print("Built in the 18th century, the church is an Orthodox church and one of the most beautiful structures reflecting the Baroque style. Its interior is dominated by red; the icons and gilded altar attract tourists. The beauty of its dark green domes, adorned with gold, is dazzling. The legend of St. Andrew's Church, built on the cliffside, is famous. Because of the belief that if the bells rang, the sea would rise and flood the city, this church lacks a bell. It has been used as a museum since 1968. You can also enter the observation platforms with a ticket, view the Dnieper River, and examine the church up close.\n")
        else:
            print("They are not ready.")
            break

        ninth_place = input("Where to next? -> 6(6): ").strip()
        if ninth_place == "6":
            print("Your choice is Andrevski Spusk\n")
            print("It connects Kontraktova and Sofia Squares. The name of the hill comes from the Andryevskaya Church, located at its base. When you look at the church, you'll immediately notice a curious feature: the church doesn't have a bell. This is due to a legend. It's believed that in the past, when Kiev was covered by sea, Andrew, one of Jesus' 12 apostles, raised a cross over the church, and the sea disappeared. The church doesn't have a bell because, according to legend, if it rings, the sea will reappear and flood Kiev. Along the hill are rows of shops selling a variety of goods and souvenirs. In the shops, you can find everything from antiques and figurines to paintings and flags, gramophones and vintage cameras. All the buildings here are old and historical.\n")
        else:
            print("They are not ready.")
            break

        print("You've finished visiting Kiev. You can choose the next city.\n")

        print("2. -> Lviv")
        print("3. -> Lutsk")
        city = input("Your choice for city? -> 2-3(3): \n ").strip()

        if not city == "3":
            print("They are not ready.")
            break

        print("You chose Lutsk. It takes 5 hours and 15 minutes by car. So you can choose a place to start your travel:\n")

        print(f"1. -> The Holy Trinity Orthodox Cathedral", "2. -> Maydan Teatralnyy", "3. -> Lubart Castle", "4. -> Lesya Ukrainka Street\n", "You chose Lutsk. It takes 5 hours and 15 minutes by car. So you can choose a place to start your travel:\n")

        place = input("Where do you want to start? -> 1-4(2):\n ").strip()
        if place == "2":
            print("Your choice is Maydan Teatralnyy\n")
            print("The square features a large statue of Lesya Ukrainka, one of Ukraine's most beloved writers. Behind Lesya is the Taras Shevchenko Regional Drama and Music Theatre. The theatre, completed in the 1930s, and the statue, erected in the 1970s, are both relatively recent additions to Lutsk's architectural and monumental landscape. After Lutsk became part of the Russian Empire in 1795, the square was used as a parade ground for Russian troops occupying the city. Once home to military barracks, the square was renovated and reclaimed in 2011. Today, events, festivals, concerts, and celebrations are held there.\n")
        else:
            print("They are not ready.")
            break

        second_place = input("Where do you want to start? -> 1-4(1):\n ").strip()
        if second_place == "1":
            print("Your choice is The Holy Trinity Orthodox Cathedral\n")
            print("The Holy Trinity Orthodox Cathedral, built in the Baroque style, was originally a complex of Catholic churches and Bernardine monasteries. The monastery was built in 1721 and completed in 1789. In the second half of the 19th century, the Bernardine monks' property was removed, and the complex was donated to the Orthodox community of Lutsk. In the 1870s, the church was rebuilt, adding a bell tower and a central dome to the narthex. The interior is polished with beeswax, and the exterior features a rose garden. The shrine within the church is dedicated to Nebesna Sotnya (those killed in Kiev during the Maidan revolution) and those who died fighting the Russians in the Donbas, recalling the turbulent times Ukraine has experienced more recently. The cathedral is a two-story, horseshoe-shaped structure with two towers in the central part of its façade. The building resembles the architecture of a palace rather than a monastery. The interior cathedral decor, preserved by a two-story, carved and gilded iconostasis built by Ukrainian masters, dates back to the 19th century.\n")
        else:
            print("They are not ready.")
            break

        third_place = input("Where do you want to start? -> 3-4(4):\n ").strip()
        if third_place == "4":
            print("Your choice is Lesya Ukrainka Street\n")
            print("It is Lutsk's most popular street. Lesya Ukrainka Street (formerly Jagiellońska – Jagiellon Street) is a pedestrian street running from the city center, Theatre Square, to Brothers' Bridge Square. The street is 730 meters long and is home to at least ten churches and monasteries. The street began to develop in the eighteenth century, when the city began to expand along it. By the early 19th century, it had become the city's main thoroughfare. The street's name was changed to Lesya Ukrainka in the 1990s. It boasts many architectural landmarks and has become a major commercial artery for the city. Numerous cafes, restaurants, banks, businesses, shops, and stores are located along the street. You can easily identify buildings built by the Polish Empire in the 17th and 18th centuries, as well as buildings from the pre-Soviet era in the 19th century, which exhibit a strong Polish influence.\n")
        else:
            print("They are not ready.")
            break

        forth_place = input("Where do you want to start? -> 3(3):\n ").strip()
        if forth_place == "3":
            print("Your choice is Lubart Castle\n")
            print("For many years, Lubart Castle served as the administrative and spiritual capital of the region. It also stands behind the Ukrainian currency of 200 hryvnias and is one of the seven wonders of Ukraine. Lutsk Castle consists of two parts: the Upper Castle, which has survived to this day, and the Lower, or Round Castle, where parts of its walls have been incorporated into other buildings and where one of its eight towers, the Czartoryski Tower, is located. Lutsk Castle is surrounded by ornate 17th-century churches and houses and is in remarkably good condition. Named Lubart Castle after the Lithuanian prince who ordered its construction, it has 13-meter-high ramparts and three tall rectangular towers, one of which houses the Bell Museum. There are also archaeological remains of a 12th-century church (St. John's Church) and a 14th-century palace, a small dungeon, and several small museums dedicated to books, bells, weapons, and local art.\n")
        else:
            print("They are not ready.")
            break

        print("You've finished visiting Lutsk. You can choose the next city.\n")
    
    while True:
        print("2. -> Lviv")
        city = input("Your choice for city? -> 2(2): \n ").strip()

        if not city == "2":
            print("They are not ready.")
            break

        print("1. -> Rynok Square")
        print("2. -> St. George's Cathedral")
        print("3. -> Ivan Franko Park")
        print("4. -> Virmenska Street")
        print("5. -> Svobody Avenue")
        print("6. -> Lviv High Castle")
        print("7. -> Stryisky Park\n")

        print("You chose Lviv. It takes 3 hours by car. So you can choose a place to start your travel:\n")

        place = input("Where do you want to start? -> 1-7(6):\n ").strip()
        if place == "6":
            print("Your choice is Lviv High Castle\n")
            print("The ruins of the castle, a circular structure originally built of wood in the 13th century, stand at an altitude of approximately 415 meters. The High Castle, transformed from wood to stone, also served as an ammunition depot and police station. To reach the High Castle, located a few kilometers from Rynok Square, you must climb long staircases and paths.\n")
        else:
            print("They are not ready.")
            break

        second_place = input("Where do you want to start? -> 1-7(4):\n ").strip()
        if second_place == "4":
            print("Your choice is Virmenska Street\n")
            print("If you're looking to experience Armenian culture, you can come here. Their journey to Lviv began in the 13th century. They settled in this area after being forced to leave their homeland by the Mongol invasion. You'll find the Armenian Cathedral, the Armenian Courtyard, old-style houses, art galleries, cafes/restaurants serving delicious local Armenian cuisine, and souvenir shops along this street.\n")
        else:
            print("They are not ready.")
            break

        third_place = input("Where do you want to start? -> 1-7(1):\n ").strip()
        if third_place == "1":
            print("Your choice is Rynok Square\n")
            print("The streets of the square are lined with numerous cafes and restaurants. These spaces are decorated with delightful details, and their designs and themes are quite striking. We've mentioned that Lviv closely resembles European tourist cities; one of the first indications of this is the presence of the town hall and clock tower in the square. Fountains are built at various corners of the square, symbolizing Neptune, Diana, Amphitria, and Adonis. While you're at Rynok Square, you can also visit the Pharmacy Museum, the Lviv Historical Museum, and the chocolate factory.\n")
        else:
            print("They are not ready.")
            break

        forth_place = input("Where do you want to start? -> 2-7(5):\n ").strip()
        if forth_place == "5":
            print("Your choice is Svobody Avenue\n")
            print("Many of the buildings are historic, and each one tells a unique story. Some people enjoy the tranquility of the square in the morning, but because it's a major traffic route, it maintains a vibrant energy throughout most of the day. You'll find everything from restaurants and cafes to cultural and artistic venues and shopping malls.\n")
        else:
            print("They are not ready.")
            break

        fifth_place = input("Where do you want to start? -> 2-7(3):\n ").strip()
        if fifth_place == "3":
            print("Your choice is Ivan Franko Park\n")
            print("Ivan Franko, Ukraine's oldest park, was built by Roman Emperor Joseph II at the end of the 18th century. Since the area was previously owned by the Jesuits, locals also call it the Jesuit Gardens.\n")
        else:
            print("They are not ready.")
            break

        sixth_place = input("Where do you want to start? -> 2-7(2):\n ").strip()
        if sixth_place == "2":
            print("Your choice is St. George's Cathedral\n")
            print("Architect Bernard Meretyn and sculptor Johann George Pinsel worked together. An architectural examination of the cathedral reveals details of the Rococo and Baroque styles. The 18th-century cathedral is one of the most beautiful religious buildings not only in the city but in Europe. Many other works are also on display, including a statue of St. George and an icon of the Virgin Mary, believed to work miracles.\n")
        else:
            print("They are not ready.")
            break

        seventh_place = input("Where do you want to start? -> 7(7):\n ").strip()
        if seventh_place == "7":
            print("Your choice is Stryisky Park\n")
            print("It's one of the first places that comes to mind when thinking of romance. As you explore the park, you'll also spot a pond with swans and ducks floating on it. You'll also see brides and grooms taking wedding photos around the pond and in the park in general.\n")
        else:
            print("They are not ready.")
            break

        print("You've finished visiting Lviv.\n")
        print("You have finished travelling Ukraine. You can choose other country.")

    while True:
        print(f"3. Russia", "4. Estonia", "5. Lithuania", "6. Belarus", "7. Poland", "8. Latvia")
        country = input("Where to next? -> 3-8(7):\n ").strip()

        if not country == "7":
            print("They are not ready.")
            break

        print("Your choice is Poland. Please choose a city:\n ")
        print(f"1. -> Lodz", "2. -> Krakow", "3. -> Gdansk", "4. -> Wroclaw", "5. -> Poznan", "6. -> Warsaw\n", "7. -> Szczecin\n")
        city = input("Your choice for city? -> 1-7:(2)\n ").strip()

        if not city == "2":
            print("They are not ready.")
            break

        print("You chose Krakow. It takes 5 hours by car. So you can choose a place to start your travel:\n")

    while True:    
        print("1. -> Wawel Castle", "2. -> Plac Nowy", "3. -> Vistulan Boulevards", "4. -> Floriańska Street", "5. -> Wawel Cathedral", "6. -> Rynek Główny", "7. -> St. Mary Basilica", "8. -> Planty Park", "9. -> Plac Bohaterów Getta\n")

        place = input("Where do you want to start? -> 1-9(9):\n ").strip()
        if place == "9":
            print("Your choice is Plac Bohaterów Getta\n")
            print("This central square in the Podgorze District, one of the most popular areas for both shopping and dining, is home to one of the city's most poignant memorials. It was the site of the Krakow ghetto from 1941 to 1943. A scene of unspeakable tragedies, the square is sure to appeal to those interested in Nazi history. In 2005, the square was redesigned, and 70 large chairs were installed in memory of the victims of the Krakow ghetto.\n")
            break

        second_place = input("Where do you want to start? -> 1-8(3):\n ").strip()
        if second_place == "3":
            print("Your choice is Vistulan Boulevards\n")
            print("Vistula is the name given to the river. The Vistulan Boulevards are a recreational area built right on the riverbank, with walking and cycling paths and docks for tour boats.\n")
        else:
            print("They are not ready.")
            break

        third_place = input("Where do you want to start? -> 1-8(2):\n ").strip()
        if third_place == "2":
            print("Your choice is Plac Nowy\n")
            print("Plac Nowy, also known as Nowy Square or New Square, is one of the liveliest and most crowded squares. Located not far from the Kazimierz district, this square becomes particularly lively at night. Its numerous cafes and bars make it a popular destination for both tourists and locals. The square also hosts an antiques market on Saturdays and a clothing market on Sundays.\n")
        else:
            print("They are not ready.")
            break

        forth_place = input("Where do you want to start? -> 1-8(1):\n ").strip()
        if forth_place == "1":
            print("Your choice is Wawel Castle\n")
            print("Its blend of Gothic, Renaissance, Rococo, and Romanesque architecture is noteworthy. The castle, which is intriguing not only for its architecture but also for its history and magnificent interior decoration, is actually a complex of many different structures. The residence of the King of Poland from the 13th to the 17th centuries, the structure has been a museum since 1940.\n")

            print(f"Opening hours: Everyday: 08.30-19.10\n, Entry fee: Regular: 55 PLN, Under 18: free\n")
        else:
            print("They are not ready.")
            break

        fifth_place = input("Where do you want to start? -> 4-8(5):\n ").strip()
        if fifth_place == "5":
            print("Your choice is Wawel Cathedral\n")
            print("Hidden behind the ancient walls of Wawel Castle, with its Baroque and Gothic façades, it is arguably Poland's most important church. Besides its magnificent architecture, this cathedral is one of the oldest religious buildings in the city, located just outside the historic city center, near the Church of Saints Peter and Paul. For many years, the cathedral hosted the coronation of kings and queens, and took its current form in the 14th century.\n")
        else:
            print("They are not ready.")
            break

        sixth_place = input("Where do you want to start? -> 4-8(8):\n ").strip()
        if sixth_place == "8":
            print("Your choice is Planty Park\n")
            print("It's a charming green space surrounding the monument-filled Old Town, which serves as the city's lungs. Covering 21,000 square meters and stretching 8 km, it's one of the largest parks in Poland. Divided by small gardens, it's the perfect place to enjoy both fresh air and tranquility in the city center.\n")
        else:
            print("They are not ready.")
            break

        seventh_place = input("Where do you want to start? -> 4-7(7):\n ").strip()
        if seventh_place == "7":
            print("Your choice is St. Mary Basilica \n")
            print("Centrally located in the heart of the Old Town, the Basilica of St. Mary was first built in the 13th century and rebuilt in the 14th century, taking its current form. Completed in 1347 during the reign of Casimir III the Great, the structure captivates visitors with its interior decorations as much as its exterior. While the frescoes are most striking in the colorful interior, almost every section inside possesses artistic value. It is decorated with carvings, sculptures, and paintings. The interior features a high altar carved in wood by Veit Stoss. The altar, with its three-panel design, holds significance because, upon its opening, it was the largest Gothic altar in the world.\n")

            print(f"Opening hours: Monday-Saturday: 11.00-18.00 and Sunday: 14.00-18.00\n, Entry fee: Regular: 20 PLN\n 8-18 children and +65: 8 PLN")
        else:
            print("They are not ready.")
            break

        eighth_place = input("Where do you want to start? -> 4-6(6):\n ").strip()
        if eighth_place == "6":
            print("Your choice is Rynek Główny\n")
            print("It's the heart of Krakow's medieval Old Town. Surrounded by magnificent architecture and home to numerous venues, the square's distinctive feature. Covering an area of 40,000 square meters, the square offers everything a tourist might need, including cafes, museums, clubs, bars, souvenir shops, historical sites, hotels, and guesthouses.\n")
        else:
            print("They are not ready.")
            break

        ninth_place = input("Where do you want to start? -> 4(4):\n ").strip()
        if ninth_place == "4":
            print("Your choice is Floriańska Street\n")
            print("This street, a favorite spot for shopaholics, was built after the Tatar invasion of 1241, like many of the city's landmarks. Starting at St. Florian's Gate at the beginning of the Royal Route, it stretches all the way to Rynek Główny, the heart of the Old Town. In addition to its extensive shopping opportunities, Florianska Street offers visitors a wonderful blend of old and new.\n")
        else:
            print("They are not ready.")
            break

        print("You've finished visiting Krakow. You can choose the next city.\n")








Travel()


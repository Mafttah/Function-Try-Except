def Travel():
    while True:
        print("Europe -> 1")
        print("Asia -> 2")
        print("South America -> 3")
        secim = input("Which continent would you like to go to? -> 1,2,3:\n ").strip()

        if not secim == "1":
            print("They are not ready.")
            break

        print("\nWhich part of Europe would you like to go?\n ")
        print("1. East Europe (Russia, Ukranie, Poland, Lithuania, Latvia, Estonia, Moldova)")
        print("2. West Europe (England, Scotland, Wales, Ireland,Northern Ireland, France, Belgium, Netherland, Germany, Luxemburg)")
        print("3. Latin Countries (Spain, Portugal, Italy")
        print("4. Scandinavian Countries (Norway, Sweden, Fınland)")
        print("5. Middle Europe Czechia, Austria, Slovenia, Slovakia)")
        print("6. Balkans (Greece, Bulgaria, Romania, Montenegro, Makedonia, Serbia, Albania, Croatia, Hungary, Slovenia, Bosnia and Herzegovina)")
        part = input("What is your choice for part of Europe? -> 1,2,3,4,5,6:\n ").strip()

        if not part == "1":
            print("They are not ready.")
            break

        print("\nYour choice is East Europe. Please choose a country:\n ")
        print("1. Moldova")
        print("2. Ukraine")
        print("3. Poland")
        print("4. Estonia")
        print("5. Lithuania")
        print("6. Russia")
        print("7. Belarus")
        print("8. Latvia")
        country = input("Your choice for country? -> 1-8:\n ").strip()

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
        print("You chose Balti. So you can choose a place to start your travel:\n ")

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
        print("3. Russia")
        print("4. Estonia")
        print("5. Lithuania")
        print("6. Belarus")
        print("7. Poland")
        print("8. Latvia")
        country = input("You have finished travelling Moldova. You can choose other country. Where to next? -> 2-8(2):\n ").strip()

        if not country == "2":
            print("They are not ready.")
            break

        print("Your choice is Ukraine. Please choose a city:\n ")
        print("1. -> Odessa")
        print("2. -> Lviv")
        print("3. -> Lutsk")
        print("5. -> Kharkiv")
        print("6. -> Kiev")
        print("7. -> Zaporijya")
        print("8. -> Donetsk")
        city = input("Your choice for city? -> 1-8:(1)\n ").strip()

        if not city == "1":
            print("They are not ready.")
            break

        print("You chose Odessa. So you can choose a place to start your travel:\n")

        print("1. -> Shevchenko Park")
        print("2. -> Potemkin Stairs")
        print("3. -> Primorskyi Boulevard")
        print("4. -> Vorontsov Palace")
        print("5. -> Monument to Catherine II")
        print("6. -> Deribasovskaya Street")
        print("7. -> City Garden")
        print("8. -> Theater square")
        place = input("Where do you want to start? -> 1-8(1):\n ").strip()

        if place == "1":
            print("Your choice is Shevchenko Park.\n")
            print("Shevchenko Park, opened in 1875, is a bit outside the city center, but it's still a must-see. Located near Lanzheron Park, the park's entrance features a Shevchenko monument and a monument to Tsar Alexander II, restored since the Soviet era.\n")
        else:
            print("They are not ready.")

        second_place = input("After travelling the Shevchenko Park, where do you want to go next? -> 2-8(8): ").strip()
        if second_place == "8":
            print("Your choice is Theater square\n")
            print("After Deribasovskaya and Primorsky Squares, it's another important square in Odessa. When you're looking for information about Odessa, the Opera House is one of the images that will undoubtedly come to mind. With its magnificent architecture, magnificent structure, and the cultural and artistic events it hosts, the Opera House is one of the city's most important structures and is just one of the architectural wonders of Teatralnaya Square.\n")

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

        print("You've finished visiting Odessa. You can choose the next city.\n")

        print("2. -> Lviv")
        print("3. -> Lutsk")
        print("5. -> Kharkiv")
        print("6. -> Kiev")
        print("7. -> Zaporijya")
        print("8. -> Donetsk")
        city = input("Your choice for city? -> 2-8:(7)\n ").strip()

        if not city == "7":
            print("They are not ready.")
            break

        print("You chose Zaporijya. It takes 6 hours by car. So you can choose a place to start your travel:\n")

        print("1. -> St. Andrew's Cathedral")
        print("2. -> Zaporizhia Sich")
        print("3. -> Preobrazhenskiy Bridge")
        place = input("Where do you want to start? -> 1-3(2):\n ").strip()

        if place == "2":
            print("Your choice is Zaporizhia Sich.\n")
            print("The Zaporizhian Sich, a group of military settlements that existed between the 16th and 18th centuries, was flooded by the construction of dams during the Soviet era. Now, in addition to its historical significance for Ukraine, it is also home to a tradition initiated by newlyweds before the ceremony.\n")
        else:
            print("They are not ready.")

        second_place = input("After travelling the Zaporizhia Sich, where do you want to go next? -> 1-3(3): ").strip()
        if second_place == "2":
            print("Your choice is Preobrazhenskiy Bridge\n")
            print("The 550-meter-long bridge, built in 1952, was considered impossible by some. Therefore, the Preobrazhensky Bridge, considered an architectural masterpiece, consists of four arches. The bridge has two floors, the upper floor for the railway line, and the lower floor for pedestrians and private trucks.\n")

        third_place_place = input("After , where next? -> 1(1): ").strip()
        if third_place_place == "1":
            print("Your choice is St. Andrew's Cathedral.\n")
            print("Built in 2001 with the help of donations, St. Andrew's Cathedral is a blend of Baroque and modern architecture. The cathedral, the city's most visited place of worship, is also considered a monument.\n")    
        else:
            print("They are not ready.")
            break

        print("You've finished visiting Zaporijya. You can choose the next city.\n")

        print("2. -> Lviv")
        print("3. -> Lutsk")
        print("5. -> Kharkiv")
        print("6. -> Kiev")
        print("8. -> Donetsk")
        city = input("Your choice for city? -> 2-8:(8)\n ").strip()

        if not city == "8":
            print("They are not ready.")
            break

        print("You chose Donetsk. It takes 4 hours by car. So you can choose a place to start your travel:\n")

        print("1. -> Pushkina Boulevard")
        print("2. -> Svyato Preobrazhensky Cathedral")
        print("3. -> Shcherbakov Park of Culture and Leisure")
        place = input("Where do you want to start? -> 1-3(3):\n ").strip()

        if place == "3":
            print("Your choice is Shcherbakov Park of Culture and Leisure.\n")
            print("You can visit Donetsk Cultural Park, considered the heart of the city. This park, one of the city's most popular spots, offers both relaxation and a pleasant time. The park boasts numerous facilities, including exclusive restaurants, cycling trails, a summer theater, a dolphin park, and a checkerboard area. It covers an area of 62 hectares.\n")
        else:
            print("They are not ready.")

        second_place = input("After travelling the Shcherbakov Park of Culture and Leisure, where do you want to go next? -> 1-2(1): ").strip()
        if second_place == "1":
            print("Your choice is Pushkina Boulevard\n")
            print("It's one of the city's most interesting spots. After a pleasant stroll along Pushkin Boulevard, lined with cafes and restaurants, you can shop in the surrounding stores.\n")

        third_place_place = input("After Pushkina Boulevard, where next? -> 2(2): ").strip()
        if third_place_place == "2":
            print("Your choice is Svyato Preobrazhensky Cathedral\n")
            print("Dating back to 1883, the cathedral is one of the most important structures that offers a firsthand glimpse into the city's historical and religious architecture. Affiliated with the Orthodox Church, the Svyato-Preobrazhensky Cathedral is the largest religious structure you'll ever see. It is also the largest structure in Ukraine.\n")    
        else:
            print("They are not ready.")
            break

        print("You've finished visiting Zaporijya. You can choose the next city.\n")

        print("2. -> Lviv")
        print("3. -> Lutsk")
        print("5. -> Kharkiv")
        print("6. -> Kiev")
        city = input("Your choice for city? -> 2-6:(5)\n ").strip()

        if not city == "5":
            print("They are not ready.")
            break

        print("You chose Kharkiv. It takes 5 hours and 30 minutes by car. So you can choose a place to start your travel:\n")

        print("1. -> Freedom Square")
        print("2. -> Pokrovsky Monastery - Svyato-Pokrovsky boy monastry")
        print("3. -> Shevchenko City Garden")
        print("4. -> Uspensky Cathedral - Assumption Cathedral")
        print("5. -> Annunciation Cathedral - Blahovishchens Kafedral")
        place = input("Where do you want to start? -> 1-5(4):\n ").strip()

        if place == "4 - Uspensky Cathedral - Assumption Cathedral":
            print("Kharkiv's oldest Orthodox cathedral, the Cathedral, is located in the Old Town district. It served as the city's main center of worship until the Annunciation Cathedral was built in 1901. Belonging to the Orthodox Church, the building reflects neoclassical style.\n")
        else:
            print("They are not ready.")

        second_place = input("After travelling the Assumption Cathedral, where do you want to go next? -> 1-5(2): ").strip()
        if second_place == "2":
            print("Your choice is Pokrovsky Monastery - Svyato-Pokrovsky boy monastry\n")
            print("Located in Kharkiv's city center, the monastery is the city's oldest structure, built in 1689. The structure, which has survived to this day, was designed in the style of traditional Ukrainian domed churches. Its architecture makes it one of the seven wonders of Kharkiv. The monastery was damaged during World War II and restored in the early 1990s.\n")

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

        print("1. -> Taras Shevchenko Park")
        print("2. -> Saint Sophia’s Cathedral")
        print("3. -> Khreshchatyk")
        print("4. -> Pechersk Lavra - Monastery of the Caves")
        print("5. -> Independence Square - Maidan Nezaleshnosti")
        print("6. -> Andrevski Spusk")
        print("7. -> Mariyinsky Palace and Park")
        print("8. -> St. Andrew’s Church")
        print("9. -> Mother Motherland\n")

        print("You chose Kiev. It takes 6 hours and 30 minutes by car. So you can choose a place to start your travel:\n")

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
            print("\n")
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
            print("\n")
        else:
            print("They are not ready.")
            break

        sixth_place = input("Where to next? -> 2-8(5): ").strip()
        if sixth_place == "5":
            print("Your choice is Maidan Nezaleshnosti\n")
            print("\n")
        else:
            print("They are not ready.")
            break

        seventh_place = input("Where to next? -> 2-8(2): ").strip()
        if seventh_place == "2":
            print("Your choice is Saint Sophia’s Cathedral\n")
            print("\n")
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
            print("It connects Kontraktova and Sofia Squares. The name of the slope comes from the Andryevskaya Church, located right at its base. When you look at the church, you'll immediately notice a curious feature: it doesn't have a bell. This is due to a legend. It's believed that in the past, when Kiev was completely covered by sea, Andrew, one of Jesus' 12 apostles, raised a cross over the church, and the sea disappeared. The church doesn't have a bell because, according to legend, if it rings, the sea will reappear and flood Kiev. Along the slope are rows of shops selling a variety of goods and souvenirs. In the shops, you can find everything from antiques and figurines to paintings and flags, gramophones and vintage cameras. All the buildings here are old and historical.\n")
        else:
            print("They are not ready.")
            break








        print("4. -> ")
        print("5. -> ")
        print("6. -> ")
        print("7. -> ")
        print("8. -> ")










        print("3. Russia")
        print("4. Estonia")
        print("5. Lithuania")
        print("6. Belarus")
        print("7. Poland")
        print("8. Latvia")
        country = input("You have finished travelling Moldova. You can choose other country. Where to next? -> 3-8(7):\n ").strip()

        if not country == "7":
            print("They are not ready.")
            break

        print("Your choice is Ukraine. Please choose a city:\n ")
        print("1. -> Lodz")
        print("2. -> Krakow")
        print("3. -> Gdansk")
        print("4. -> Sopot")
        print("5. -> Wroclaw")
        print("6. -> Poznan")
        print("7. -> Warsaw")
        city = input("Your choice for city? -> 1-7:()\n ").strip()

        if not city == "1":
            print("They are not ready.")
            break

        print("You chose Odessa. So you can choose a place to start your travel:\n")

    


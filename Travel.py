# TODO: Best practice olarak en kısa function en iyi functiondur, en uzun function çöptür.

def Travel():
    while True:
        print("Europe -> 1")
        print("Asia -> 2")
        print("South America -> 3")
        secim = input("Which continent would you like to go to? -> 1,2,3:\n ").strip()

        if not secim == "1":
            print("They are not ready.")
            break

        while True:

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

            while True:

                print("\nYour choice is East Europe. Please choose a country:\n ")
                print(f"1. Moldova", "2. Ukraine", "3. Poland", "4. Estonia")
                print("5. Lithuania")
                print("6. Russia")
                print("7. Belarus")
                print("8. Latvia")
                country = input("Your choice for country? -> 1-8:\n ").strip()

                if not country == "1":
                    print("They are not ready.")

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
            break

        print("You've finished visiting Chisinau. You can choose the next city.\n")

        print("4. Balti")
        print("5. Soroca")
        city = input("Your choice for city? -> 4-5(4):\n ").strip()

        if not city == "4":
            print("They are not ready.")
            break
        print("You chose Balti. So you can choose a place to start your travel:\n ")

        print("1. -> St Constantin and Helena Cathedral")
        print("2. -> St. Nicolae Cathedral Balti")
        place = input("Where do you want to start? -> 1-2(1):\n ").strip()

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

        print("1. -> The Holy Trinity Orthodox Cathedral")
        print("2. -> Maydan Teatralnyy")
        print("3. -> Lubart Castle")
        print("4. -> Lesya Ukrainka Street\n")
        print("You chose Lutsk. It takes 5 hours and 15 minutes by car. So you can choose a place to start your travel:\n")

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
            break

        second_place = input("Where do you want to start? -> 1-7(4):\n ").strip()
        if second_place == "4":
            print("Your choice is Virmenska Street\n")
            print("If you're looking to experience Armenian culture, you can come here. Their journey to Lviv began in the 13th century. They settled in this area after being forced to leave their homeland by the Mongol invasion. You'll find the Armenian Cathedral, the Armenian Courtyard, old-style houses, art galleries, cafes/restaurants serving delicious local Armenian cuisine, and souvenir shops along this street.\n")
            break

        third_place = input("Where do you want to start? -> 1-7(1):\n ").strip()
        if third_place == "1":
            print("Your choice is Rynok Square\n")
            print("The streets of the square are lined with numerous cafes and restaurants. These spaces are decorated with delightful details, and their designs and themes are quite striking. We've mentioned that Lviv closely resembles European tourist cities; one of the first indications of this is the presence of the town hall and clock tower in the square. Fountains are built at various corners of the square, symbolizing Neptune, Diana, Amphitria, and Adonis. While you're at Rynok Square, you can also visit the Pharmacy Museum, the Lviv Historical Museum, and the chocolate factory.\n")
            break

        forth_place = input("Where do you want to start? -> 2-7(5):\n ").strip()
        if forth_place == "5":
            print("Your choice is Svobody Avenue\n")
            print("Many of the buildings are historic, and each one tells a unique story. Some people enjoy the tranquility of the square in the morning, but because it's a major traffic route, it maintains a vibrant energy throughout most of the day. You'll find everything from restaurants and cafes to cultural and artistic venues and shopping malls.\n")
            break

        fifth_place = input("Where do you want to start? -> 2-7(3):\n ").strip()
        if fifth_place == "3":
            print("Your choice is Ivan Franko Park\n")
            print("Ivan Franko, Ukraine's oldest park, was built by Roman Emperor Joseph II at the end of the 18th century. Since the area was previously owned by the Jesuits, locals also call it the Jesuit Gardens.\n")
            break

        sixth_place = input("Where do you want to start? -> 2-7(2):\n ").strip()
        if sixth_place == "2":
            print("Your choice is St. George's Cathedral\n")
            print("Architect Bernard Meretyn and sculptor Johann George Pinsel worked together. An architectural examination of the cathedral reveals details of the Rococo and Baroque styles. The 18th-century cathedral is one of the most beautiful religious buildings not only in the city but in Europe. Many other works are also on display, including a statue of St. George and an icon of the Virgin Mary, believed to work miracles.\n")
            break

        seventh_place = input("Where do you want to start? -> 7(7):\n ").strip()
        if seventh_place == "7":
            print("Your choice is Stryisky Park\n")
            print("It's one of the first places that comes to mind when thinking of romance. As you explore the park, you'll also spot a pond with swans and ducks floating on it. You'll also see brides and grooms taking wedding photos around the pond and in the park in general.\n")
            break

        print("3. Russia")
        print("4. Estonia")
        print("5. Lithuania")
        print("6. Belarus")
        print("7. Poland")
        print("8. Latvia")
        country = input("You have finished travelling Ukraine. You can choose other country. Where to next? -> 3-8(7):\n ").strip()

        if not country == "7":
            print("They are not ready.")
            break

        print("Your choice is Poland. Please choose a city:\n ")
        print("1. -> Lodz")
        print("2. -> Krakow")
        print("3. -> Gdansk")
        print("4. -> Wroclaw")
        print("5. -> Poznan")
        print("6. -> Warsaw\n")
        print("7. -> Szczecin\n")
        city = input("Your choice for city? -> 1-7:(2)\n ").strip()

        if not city == "2":
            print("They are not ready.")
            break

        print("You chose Krakow. It takes 5 hours by car. So you can choose a place to start your travel:\n")

        print("1. -> Wawel Castle")
        print("2. -> Plac Nowy")
        print("3. -> Vistulan Boulevards")
        print("4. -> Floriańska Street")
        print("5. -> Wawel Cathedral")
        print("6. -> Rynek Główny")
        print("7. -> St. Mary Basilica")
        print("8. -> Planty Park")
        print("9. -> Plac Bohaterów Getta\n")
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

        print("1. -> Lodz")
        print("3. -> Gdansk")
        print("5. -> Wroclaw")
        print("6. -> Poznan")
        print("7. -> Warsaw")
        print("8. -> Szczecin\n")
        city = input("Your choice for city? -> 1-8(5): \n ").strip()

        if not city == "5":
            print("They are not ready.")
            break

        print("You chose Wroclaw. It takes 4 hours by car. So you can choose a place to start your travel:\n")

        print("1. -> Wroclaw Rynek")
        print("2. -> Most Tumski Bridge")
        print("3. -> Stare Miasto")
        print("4. -> Ostrów Tumski\n")

        place = input("Where do you want to start? -> 1-4(4):\n ").strip()
        if not place == "4":
            print("Your choice is Ostrów Tumski\n")
            print("The name given to the area where the city's important cathedrals are located. Cathedral Island, reached by crossing the Tumski Bridge, is the city's oldest historical site. According to information from various archaeological excavations, settled life here is thought to date back approximately 1,000 years.\n")
        else:
            print("They are not ready.")
            break

        second_place = input("Where do you want to start? -> 1-3(2):\n ").strip()
        if not second_place == "2":
            print("Your choice is Most Tumski\n")
            print("Located on the northern side of the Oder River, the Tumski Bridge was built in 1889. It replaced a previous wooden bridge. It is also known as the Lovers' Bridge or the Cathedral Island Bridge.\n")
        else:
            print("They are not ready.")
            break

        third_place = input("Where do you want to start? -> 1-3(1):\n ").strip()
        if not third_place == "1":
            print("Your choice is Wroclaw Rynek\n")
            print("This square is a market square in Wrocław dating back to medieval times. It was established between 1214 and 1232 under Magdeburg law during the reign of the Polish Duke Henry I the Bearded. The two largest town halls in the country are located here. It is also one of the largest market squares in Europe. In the 1800s, the square was connected to tram lines, initially a horse-drawn system but electrified after 1892. The market square was damaged during World War II, but most of the buildings survived and were later carefully restored.\n")
        else:
            print("They are not ready.")
            break

        forth_place = input("Where do you want to start? -> 3(3):\n ").strip()
        if not forth_place == "3":
            print("Your choice is Stare Miasto\n")
            print("Market Square, known as the Rynek, is one of the largest in Europe. Surrounded by historic buildings, this square is always a hub for cultural activity. Restaurants and historic shopping venues are located here. The historic Ratusz Town Hall, with its Gothic architecture, is also a symbol of the city. This 13th-century structure has evolved over time, developing into its current form. Having survived World War II with minimal damage, the building now houses the Museum of Bourgeois Art. The Royal Palace, Palac Krolewski, is a Baroque structure located south of the Old Town. Built by the Austrians in 1717, it served as the residence of Prussia's renowned King Frederick the Great. The famous German iron medallion was born here in 1813. It currently serves as a museum.\n")
        else:
            print("They are not ready.")
            break

        print("You've finished visiting Wroclaw. You can choose the next city.\n")

        print("1. -> Lodz")
        print("3. -> Gdansk")
        print("6. -> Poznan")
        print("7. -> Warsaw")
        print("8. -> Szczecin\n")
        city = input("Your choice for city? -> 1-8(6): \n ").strip()
        if not city == "6":
            print("They are not ready.")
            break

        print("You chose Poznan. It takes 2 hours and 30 minutes hours by car. So you can choose a place to start your travel:\n")

        print("1. -> Poznań Fara")
        print("2. -> Stary Rynek")
        print("3. -> Zamek Castle - Royal Castle")
        print("4. -> Ulica Wroclawska")
        print("5. -> Swiety Marcin\n")

        place = input("Where do you want to start? -> 1-5(1):\n ").strip()
        if not place == "1":
            print("Your choice is Poznań Fara\n")
            print("Its architecture and interior design make it one of Poland's most beautiful Baroque monuments. Construction began on this magnificent church in the 17th century and took approximately 80 years to complete. The church's exterior boasts a simple yet impressive Baroque design. A look at its history reveals that the building was not just a place of worship but also holds a significant place in the city's cultural heritage. During the Napoleonic era, the church served as a shelter and has witnessed Poland's various challenging periods.\n")
        else:
            print("They are not ready.")
            break

        second_place = input("Where do you want to start? -> 2-5(4):\n ").strip()
        if not second_place == "4":
            print("Your choice is Ulica Wroclawska\n")
            print("One of the city's liveliest and most entertaining spots. Lined with colorful buildings, this lively street is home to bars, cafes, and restaurants.\n")
        else:
            print("They are not ready.")
            break

        third_place = input("Where do you want to start? -> 2-5(2):\n ").strip()
        if not third_place == "2":
            print("Your choice is Stary Rynek\n")
            print("The heart of Poznan. Located in the historic old town of Stare Miasto, this charming square boasts colorful 16th-century Renaissance-style houses, cobblestone backstreets, cafes, and restaurants, making it a prime tourist attraction. It's also famous for the fountains of Neptune, Apollo, Mars, and Proserpine, as well as the statues of Jana Nepomuceno and Preigerz, scattered throughout the square.\n")
        else:
            print("They are not ready.")
            break

        forth_place = input("Where do you want to start? -> 3-5(3):\n ").strip()
        if not forth_place == "3":
            print("Your choice is Zamek Castle - Royal Castle\n")
            print("Built for German Emperor Wilhelm II and passed from hand to hand for a long time, this complex, built in the Romanesque style, served as the headquarters of Poznan University after the emperor's use, Hitler's official residence after the occupation, and the seat of local government after the war. It now serves as a Cultural Center.\n")
        else:
            print("They are not ready.")
            break

        fifth_place = input("Where do you want to start? -> 5(5):\n ").strip()
        if not fifth_place == "5":
            print("Your choice is Swiety Marcin\n")
            print("It's one of Poznań's most important streets, filled with shopping malls, cafes, and restaurants. It's one of Poznań's liveliest and most vibrant areas, showcasing the city's modern face. Starting from Poznań Castle and extending towards the city center, the street is a meeting point for both locals and tourists.\n")
        else:
            print("They are not ready.")
            break

        print("You've finished visiting Poznan. You can choose the next city.\n")

        print("1. -> Lodz")
        print("3. -> Gdansk")
        print("7. -> Warsaw")
        print("8. -> Szczecin\n")

        city = input("Your choice for city? -> 1-8(8): \n ").strip()
        if not city == "8":
            print("They are not ready.")
            break

        print("You chose Szczecin. It takes 3 hours by car. So you can choose a place to start your travel:\n")

        print("1. -> Kasprowicz Park")
        print("2. -> Jasne Błonia")
        print("3. -> Castle of the Pomeranian Dukes")
        print("4. -> Stare Miasto\n")

        place = input("Where do you want to start? -> 1-4(3):\n ").strip()
        if not place == "3":
            print("Your choice is Castle of the Pomeranian Dukes\n")
            print("Located in the historic heart of Szczecin, it sheds light on the city's past. This Renaissance castle is now used for exhibitions and events. It's also an ideal venue for art and history enthusiasts.\n")
            print(f"Opining Hours: 10.00-18.00\n Entry fee: 30 PLN")
        else:
            print("They are not ready.")
            break

        place = input("Where do you want to start? -> 1-4(4):\n ").strip()
        if not place == "4":
            print("Your choice is Stare Miasto\n")
            print("With its colorful buildings and narrow streets, the Old Town will give you a sense of Szczecin's historical heritage. Here, you'll find traces of the past and some fantastic photos.\n")
        else:
            print("They are not ready.")
            break

        place = input("Where do you want to start? -> 1-2(2):\n ").strip()
        if not place == "2":
            print("Your choice is Jasne Błonia\n")
            print("This expansive green space in the city center is the ideal place to relax and enjoy nature. Enjoy a picnic in the shade of the trees or simply relax and observe the surroundings. It also hosts a variety of outdoor activities.\n")
        else:
            print("They are not ready.")
            break

        place = input("Where do you want to start? -> 1(1):\n ").strip()
        if not place == "":
            print("Your choice is Kasprowicz Park\n")
            print("One of the city's largest parks, it stands out for its natural beauty and peaceful atmosphere. You can stroll around the pond and observe local flora and fauna.\n")
        else:
            print("They are not ready.")
            break

        print("You've finished visiting Szczecin. You can choose the next city.\n")

        print("1. -> Lodz")
        print("3. -> Gdansk")
        print("7. -> Warsaw")

        city = input("Your choice for city? -> 1-7(3):\n ").strip()
        if not city == "3":
            print("They are not ready.")
            break

        print("You chose Gdansk. It takes 5 hours and 30 minutes hours by car. So you can choose a place to start your travel:\n")

        print("1. -> Ulica Mariacka")
        print("2. -> Dlugi Targ")
        print("3. -> St. Mary's Church\n")

        place = input("Where do you want to start? -> 1-3(1):\n ").strip()
        if not place == "1":
            print("Your choice is Ulica Mariacka\n")
            print("With its narrow, ornately decorated houses lined up side by side, it was once the subject of novels and films. Although severely damaged during World War II, it has since been rebuilt.")
        else:
            print("They are not ready.")
            break

        second_place = input("Where do you want to start? -> 2-3(3):\n ").strip()
        if not second_place == "3":
            print("Your choice is St. Mary's Church\n")
            print("One of Gdańsk's most recognizable buildings, it is the largest brick church in Europe and is in the Gothic style.")
        else:
            print("They are not ready.")
            break

        third_place = input("Where do you want to start? -> 2(2):\n ").strip()
        if not third_place == "2":
            print("Your choice is Dlugi Targ\n")
            print("Dugi Targ (Long Market) is a completely pedestrianized square, adorned with 17th-century buildings and adorned with Baroque city gates. This section of the city is called the Royal Route, so named because in ancient times, visiting kings would enter the city in processions through these gates.")
        else:
            print("They are not ready.")
            break

        print("You've finished visiting Szczecin. You can choose the next city.\n")

        print("1. -> Lodz")
        print("7. -> Warsaw")

        city = input("Your choice for city? -> 1(1):\n ").strip()
        if not city == "1":
            print("They are not ready.")
            break

        print("You chose Lodz. It takes 5 hours and 20 minutes hours by car. So you can choose a place to start your travel:\n")

        print("1. -> Piotrkowska Street")
        print("2. -> Izrael Poznański Palace\n")

        place = input("Where do you want to start? -> 1-2(2):\n ").strip()
        if not place == "2":
            print("Your choice is Izrael Poznański Palace\n")
            print("It's home to the Lodz City Museum, where you can explore the city's rich history and cultural heritage.")
        else:
            print("They are not ready.")
            break

        place = input("Where do you want to start? -> 1(1):\n ").strip()
        if not place == "1":
            print("Your choice is Piotrkowska Street\n")
            print("This street, the symbol of Łódź, is located in the city center. It is approximately 4 km long and runs in a straight line north and south between Plac Wolnosci and Plac Niepodlegtosci. The entire city has developed around it throughout history. This development pattern has shaped the city center into its current form. Initially a mere transportation route, the street has evolved over time into the city's main attraction, a commercial and entertainment center, and the focal point of a growing industrial development. Currently home to over 100 bars and restaurants, it is the longest and most fully pedestrianized street in Poland and also hosts numerous shops. During the peak tourist season in summer, the gardens along the street, with their vibrant landscapes, offer a delightful resting spot for both the eyes and tired bodies. On foot or by tram, you can get a close-up view of architectural structures like Trzej Fabrykanci (Three Manufacturers), Laweczka Tuwima (Tuwim's Bank), or the Pomnik kodzian Pretomu Tysi cleci (Monument to the People of Łódź at the Turn of the Millennium), comprised of 12,859 apartment blocks, each with their names inscribed on them.")
        else:
            print("They are not ready.")
            break

        print("You've finished visiting Szczecin. You can choose the next city.\n")

        print("7. -> Warsaw")

        city = input("Your choice for city? -> 7(7):\n ").strip()
        if not city == "7":
            print("They are not ready.")
            break

        print("You chose Warsaw. It takes 3 hours by car. So you can choose a place to start your travel:\n")

        print("1. -> Old Town Square")
        print("2. -> Saxon Garden")
        print("3. -> Castle Square - Plac Zamkowy")
        print("4. -> Krakowskie Przedmieście")
        print("5. -> Royal Castle")
        print("6. -> National Museum in Warsaw")
        print("7. -> Nowy Świat Street")
        print("8. -> Wilanów Palace")
        print("9. -> Łazienki Park")
        print("10. -> Łazienki Palace")
        print("11. -> Sigismund's Column")
        print("12. -> Palace of Culture and Science")
        print("13. -> Warsaw New Town")
        print("14. -> Taras Widokowy St Anne\n")
        print("15. -> Krasinski Palace")

        place = input("Where do you want to start? -> ():\n ").strip()
        if not place == "":
            print("Your choice is \n")
            print("")
        else:
            print("They are not ready.")
            break

        second_place = input("Where do you want to start? -> ():\n ").strip()
        if second_place == "":
            print("Your choice is \n")
            print("\n")
        else:
            print("They are not ready.")
            break

        third_place = input("Where do you want to start? -> ():\n ").strip()
        if third_place == "":
            print("Your choice is \n")
            print("\n")
            break

        forth_place = input("Where do you want to start? -> ():\n ").strip()
        if forth_place == "":
            print("Your choice is \n")
            print("\n")

        else:
            print("They are not ready.")
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
            break

        fifteenth_place = input("Where do you want to start? -> ():\n ").strip()
        if fifteenth_place == "":
            print("Your choice is \n")
            print("\n")
            break









        





        print("2. Ukraine")
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

        

        place = input("Where do you want to start? -> ():\n ").strip()
        if not place == "":
            print("Your choice is ...\n")
            print("\n")
        else:
            print("They are not ready.")
            break

        place = input("Where do you want to start? -> ():\n ").strip()
        if not place == "":
            print("\n")
            print("\n")
        else:
            print("They are not ready.")
            break

        print("1. -> Lodz")
        print("3. -> Gdansk")
        print("4. -> Sopot")
        print("5. -> Wroclaw")
        print("6. -> Poznan")
        print("7. -> Warsaw")
        print("8. -> Szczecin\n")
        city = input("Your choice for city? -> 1-8(5): \n ").strip()

        if not city == "5":
            print("They are not ready.")
            break

        print("You chose Wroclaw. It takes 4 hours by car. So you can choose a place to start your travel:\n")

        print("1. -> ")
        print("2. -> ")
        print("3. -> ")
        print("4. -> ")
        print("5. -> ")
        print("6. -> ")
        print("7. -> ")
        print("8. -> ")
        print("9. -> \n")
        print("5. -> ")
        print("6. -> ")
        print("7. -> ")
        print("8. -> ")
        print("9. -> ")

Travel()
    


# Maçları saklayacağımız liste
all_matches = []
# Todo: Players functionında oyuncular uygun bir tipte değişkende saklanacak şekilde güncellenmelidir. Burada players functionun içinde oyuncu adları sadece print ile gösteriliştir. 
# dict in içinde oyunculara bir Id vererek snake_case formatıyla key kullanarak idct oluşturmak gerekiyor. (oyuncu sıra ID, oyuncu adı, oyuncu soyadı.)
# Players ın içindekileri ayrıca kullanıcıya listeleyen for ile bir function yazılacak

def main_menu():
    while True:
        # Ana menü
        print("--- Wimbledon Championship Tracker ---")
        print("1. Add New Match")
        print("2. List All Matches")
        print("3. View Player Statistics")
        print("4. Show Tournament Summary")
        print("5. List_all_players")
        print("6. Exit")
        print("--------------------------------------")

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.\n")
            continue

        # Seçime göre ilgili fonksiyonlar çağrılır
        if choice == 1:
            add_match()
        if choice == 2:
            list_matches()
        if choice == 3:
            player_statistics()
        if choice == 4:
            tournament_summary()
        if choice == 5:
            list_all_players()
        if choice == 6:
            print("Exiting the program")
            break
        else:
            print("Please enter a valid choice between 1 and 5.\n")

# def players():
#     print("Men players\n")
#     print("Pedro Martínez")
#     print("Jaume Munar")
#     print("Alejandro Davidoviç Fokina")
#     print("João Fonseca")
#     print("Luca Nardi")
#     print("Yoshihito Nishioka")
#     print("Sebastián Báez")
#     print("Beibit Zhukayev")
#     print("Roberto Carballés Baena")
#     print("Alex Michelsen")
#     print("Giovanni Mpetshi Perricard")
#     print("Aleksey Popirin")
#     print("Francisco Cerúndolo") 
#     print("Matteo Berrettini")
#     print("Holger Rünü")
#     print("Hugo Dellien")
#     print("Laslo Djere")
#     print("Jannik Sinner")
#     print("Carlos Alcaraz")
#     print("Novak Djokovic\n")

#     print("Women Players\n")

#     print("Iga Świątek")
#     print("Sonay Kartal")
#     print("Jessica Bouzas Maneiro")
#     print("Aryna Sabalenka")
#     print("Belinda Bencic")
#     print("Laura Siegemund")
#     print("Emma Navarro")
#     print("Elise Mertens")
#     print("Emma Raducanu")
#     print("Renata Zarazúa")
#     print("Kamilla Rakhimova")
#     print("Hailey Baptiste")
#     print("Danielle Collins")
#     print("Liudmila Samsonova")
#     print("Marie Bouzková")
#     print("Katie Coulter")
#     print("Eva Lys")
#     print("Yasemin Paolini")

# players()

male_players = [
    {'player_id': 1, 'first_name': 'Pedro', 'last_name': 'Martínez'},
    {'player_id': 2, 'first_name': 'Jaume', 'last_name': 'Munar'},
    {'player_id': 3, 'first_name': 'Alejandro', 'last_name': 'Davidoviç Fokina'},
    {'player_id': 4, 'first_name': 'João', 'last_name': 'Fonseca'},
    {'player_id': 5, 'first_name': 'Luca', 'last_name': 'Nardi'},
    {'player_id': 6, 'first_name': 'Yoshihito', 'last_name': 'Nishioka'},
    {'player_id': 7, 'first_name': 'Sebastián', 'last_name': 'Báez'},
    {'player_id': 8, 'first_name': 'Beibit', 'last_name': 'Zhukayev'},
    {'player_id': 9, 'first_name': 'Roberto', 'last_name': 'Carballés Baena'},
    {'player_id': 10, 'first_name': 'Alex', 'last_name': 'Michelsen'},
    {'player_id': 11, 'first_name': 'Giovanni', 'last_name': 'Mpetshi Perricard'},
    {'player_id': 12, 'first_name': 'Aleksey', 'last_name': 'Popirin'},
    {'player_id': 13, 'first_name': 'Francisco', 'last_name': 'Cerúndolo'},
    {'player_id': 14, 'first_name': 'Matteo', 'last_name': 'Berrettini'},
    {'player_id': 15, 'first_name': 'Holger', 'last_name': 'Rünü'},
    {'player_id': 16, 'first_name': 'Hugo', 'last_name': 'Dellien'},
    {'player_id': 17, 'first_name': 'Laslo', 'last_name': 'Djere'},
    {'player_id': 18, 'first_name': 'Jannik', 'last_name': 'Sinner'},
    {'player_id': 19, 'first_name': 'Carlos', 'last_name': 'Alcaraz'},
    {'player_id': 20, 'first_name': 'Novak', 'last_name': 'Djokovic'}
]

# Kadın oyuncular (Women Players)
female_players = [
    {'player_id': 21, 'first_name': 'Iga', 'last_name': 'Świątek'},
    {'player_id': 22, 'first_name': 'Sonay', 'last_name': 'Kartal'},
    {'player_id': 23, 'first_name': 'Jessica', 'last_name': 'Bouzas Maneiro'},
    {'player_id': 24, 'first_name': 'Aryna', 'last_name': 'Sabalenka'},
    {'player_id': 25, 'first_name': 'Belinda', 'last_name': 'Bencic'},
    {'player_id': 26, 'first_name': 'Laura', 'last_name': 'Siegemund'},
    {'player_id': 27, 'first_name': 'Emma', 'last_name': 'Navarro'},
    {'player_id': 28, 'first_name': 'Elise', 'last_name': 'Mertens'},
    {'player_id': 29, 'first_name': 'Emma', 'last_name': 'Raducanu'},
    {'player_id': 30, 'first_name': 'Renata', 'last_name': 'Zarazúa'},
    {'player_id': 31, 'first_name': 'Kamilla', 'last_name': 'Rakhimova'},
    {'player_id': 32, 'first_name': 'Hailey', 'last_name': 'Baptiste'},
    {'player_id': 33, 'first_name': 'Danielle', 'last_name': 'Collins'},
    {'player_id': 34, 'first_name': 'Liudmila', 'last_name': 'Samsonova'},
    {'player_id': 35, 'first_name': 'Marie', 'last_name': 'Bouzková'},
    {'player_id': 36, 'first_name': 'Katie', 'last_name': 'Coulter'},
    {'player_id': 37, 'first_name': 'Eva', 'last_name': 'Lys'},
    {'player_id': 38, 'first_name': 'Yasemin', 'last_name': 'Paolini'}
]

def list_all_players():
    print("--- Male Players ---")
    for player in male_players:
        print(f"ID: {player['player_id']:>2} | Name: {player['first_name']} {player['last_name']}")

    print("\n--- Female Players ---")
    for player in female_players:
        print(f"ID: {player['player_id']:>2} | Name: {player['first_name']} {player['last_name']}")
    print("\n-------------------------\n")



# Maç ekleme foksiyonu
def add_match():
    while True:
        print("--- Add Match ---")
        # Kullanıcıdan maç bilgileri isteniyor
        round_name = input("Enter match round (e.g., Group A 1st Match or  Quarter Final): ").strip()
        if not round_name:
            print("Write Round.")
            continue
        break

    while True:
        player1 = input("Enter Player 1 name: ")
        if not player1:
                print("Please write Player1.")
                continue
        break

    while True:
        player2 = input("Enter Player 2 name: ")
        if not player2:
                print("Please write Player2.")
                continue
        break

    while True:
        score = input("Enter match score (e.g., 6-3, 4-6, 7-5): ").strip()
        if not score:
                print("Please write Score.")
                continue
        break

    while True:
        winner = input("Enter winner's name: ")
        if not winner:
                print("Please write winner.")
                continue
        break

    # Dict tipinde match içine kullanıcıdan topladığım bilgileri ilgili keylere modelliyorum.
    match = {
        'round': round_name,
        'player1': player1,
        'player2': player2,
        'score': score,
        'winner': winner
        }

    all_matches.append(match)
print("Match added successfully!\n")
# Mustafa abiyle bunu yorum satırı yaptık.
# add_match()

# Maçları listeleme fonksiyonu

def list_matches():
    print("--- All Recorded Matches ---")
    if not all_matches:
        print("No matches recorded yet.\n")
    else:
# Tüm maçları sırayla ekrana yaz
        for match in all_matches:
            print(f"[{match['round']}] {match['player1']} vs {match['player2']} | Score: {match['score']} | Winner: {match['winner']}")

# Mustafa abiyle bunu yorum satırı yaptık.
# list_matches()

# Oyuncu istatistikleri fonksiyonu

def player_statistics():
    print("--- Player Statistics ---")
    player = input("Enter the player's name to view statistics: ").strip()
    total = 0
    wins = 0
    losses = 0

    for match in all_matches:
        if player == match['player1'] or player == match['player2']:
            total += 1
            if player == match['winner']:
                wins += 1
            else:
                losses += 1

    if total == 0:
        print(f"No records found for player '{player}'. Please make sure the name is correct.\n")
    else:
        print(f"\nStatistics for {player}:")
        print(f"Total Matches Played: {total}")
        print(f"Matches Won: {wins}")
        print(f"Matches Lost: {losses}")
        win_percent = (wins / total) * 100
        print(f"Win Percentage: {win_percent:}%\n")


# Mustafa abiyle bunu yorum satırı yaptık.
# player_statistics()

# Turnuva özeti fonksiyonu
    # Birden fazla maçı göstermiyor. Kontrol edilecek.

def tournament_summary():
    # Fast fail ile başarısızlıkları yakalayıp return ile çıkıyoruz.(Bu bir best practice dir.)
    if not all_matches:
        print("No matches to summarize.\n")
        return
    
    print("--- Tournament Summary ---")
    total_matches = len(all_matches)
    print(f"Total Matches Played: {total_matches}\n")

    print("All Matches:")
    for match in all_matches:
        sets = match['score'].split(',')
        set_count = len(sets)
        print(f"[{match['round']}] {match['player1']} vs {match['player2']} | Score: {match['score']} | Winner: {match['winner']} ({set_count} sets)")

    print("\n--- Longest Match(es) ---")
    # Aynı anda en uzun maçı gösterir
    longest_matches = []
    max_sets = 0

    for match in all_matches:
        sets = match['score'].split(',')
        set_count = len(sets)
        if set_count > max_sets:
            max_sets = set_count
            longest_matches = [match]
        elif set_count == max_sets:
            longest_matches.append(match)

    for match in longest_matches:
        print(f"[{match['round']}] {match['player1']} vs {match['player2']} | Score: {match['score']} | Winner: {match['winner']} ({max_sets} sets)\n")

# Mustafa abiyle bunu yorum satırı yaptık.
# tournament_summary()    


main_menu()


# TODO: sola yasla < işareti, sağa yasla > işareti, ortaya hizala ^ işareti
# TODO: renklendirmeleri yap.
# TODO: skorları ayıklayan bir tane fonksiyon yazılması lazım. 
# TODO: Girilen skorları oyuncu bazında Wimbledon maç hesaplama yöntemlerine göre oyuncuya aktarıp gerekli karşılaştırmaları yapmak gerekiyor. 






















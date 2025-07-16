# Maçları saklayacağımız liste
all_matches = []

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
                print("Write Player1.")
                continue
        break
    while True:
        player2 = input("Enter Player 2 name: ")
        if not player2:
                print("Write Player2.")
                continue
        break
    while True:
        score = input("Enter match score (e.g., 6-3, 4-6, 7-5): ").strip()
        if not score:
                print("Write Score.")
                continue
        break
    while True:
        winner = input("Enter winner's name: ")
        if not winner:
                print("Write winner.")
                continue
        break
    
    match = {
        'round': round_name,
        'player1': player1,
        'player2': player2,
        'score': score,
        'winner': winner
        }

    all_matches.append(match)
print("Match added successfully!\n")

add_match()

# Maçları listeleme fonksiyonu

def list_matches():
    print("--- All Recorded Matches ---")
    if not all_matches:
        print("No matches recorded yet.\n")
    else:
# Tüm maçları sırayla ekrana yaz
        for match in all_matches:
            print(f"[{match['round']}] {match['player1']} vs {match['player2']} | Score: {match['score']} | Winner: {match['winner']}")

list_matches()

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


player = player_statistics()

# Turnuva özeti fonksiyonu

def tournament_summary():
    print("--- Tournament Summary ---")
    total_matches = len(all_matches)
    print(f"Total Matches Played: {total_matches}")

    longest_match = None
    max_sets = 0

    for match in all_matches:
        sets = match['score'].split(',')
        set_count = len(sets)
        if set_count > max_sets:
            max_sets = set_count
            longest_match = match

    if longest_match:
        print("Longest Match (by Number of Sets):")
        print(f"[{longest_match['round']}] {longest_match['player1']} vs {longest_match['player2']} | Score: {longest_match['score']} | Winner: {longest_match['winner']} ({max_sets} sets)")
    print("---------------------------\n")


def main_menu():
    while True:
        print("--- Wimbledon Championship Tracker ---")
        print("1. Add New Match")
        print("2. List All Matches")
        print("3. View Player Statistics")
        print("4. Show Tournament Summary")
        print("5. Exit")
        print("--------------------------------------")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.\n")
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
            print("Exiting the program")
            break
        else:
            print("Please enter a valid choice between 1 and 5.\n")
























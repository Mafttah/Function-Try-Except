# Maçları saklayacağımız liste
all_matches = []

# Maç ekleme foksiyonu
def add_match():
    while True:
        print("--- Add Match ---")
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

def list_matches():
    print("--- All Recorded Matches ---")
    if not all_matches:
        print("No matches recorded yet.\n")
    else:
        for match in all_matches:
            print(f"[{match['round']}] {match['player1']} vs {match['player2']} | Score: {match['score']} | Winner: {match['winner']}")

list_matches()

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





























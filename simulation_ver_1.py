# In this simulation you will be playing as Player 1
# You get to pick the total number of players including yourself
# You get to pick the buy-in for other players

# TODO: Implement loop with dealer dealing right of index

import random

suits = ["Spade", "Heart", "Club", "Diamond"]
values = ["2","3","4","5","6","7","8","9","10","J", "Q", "K", "A"]

pot = 0
min_buyin_size = 40
big_blind_index = 0

print("Starting game...")
num_players = int(input("How many players: "))
print(f"Starting game with {num_players} players...")
players = [ f"Player{i+1}" for i in range(num_players) ]
print(players)

player_hands = [[] for _ in range(num_players)]
player_stacks = []
position = 0

def init_buyin():
    for i in range(num_players):
        buy_in = int(input(f"Player {i+1}'s buy-in value: "))
        while buy_in < 40 and buy_in % min_buyin_size != 0:
            print(f"Initial buy-in size is at least {min_buyin_size} and must be a multiple of {min_buyin_size}")
            buy_in = int(input(f"Re-enter Player {i+1}'s buy-in value: "))
        player_stacks.append(buy_in)
    print()
    
def buy_in(player, amount):
    while amount < 40 and amount % min_buyin_size != 0:
        print(f"Initial buy-in size is at least {min_buyin_size} and must be a multiple of {min_buyin_size}")
        amount = int(input(f"Re-enter Player {player}'s buy-in value: "))
    player_stacks[player - 1] += amount

def init_deck():
    deck = [f"{value} of {suit}" for suit in suits for value in values]
    print(f"Deck of {len(deck)} has been initialized..")
    random.shuffle(deck)
    print("Deck has been shuffled.")
    print(f"Current deck: {deck}")
    return deck

def deal_cards(deck, num):
    for i in range(2):
        for j in range(num):
            player_hands[j].append(deck.pop())
    print("All cards have been dealt")
    
def calculate_position():
    position = int(input("What is your position from the dealer: "))
    if position >= num_players // 2:  
        PB = 3
    else:
        PB = 0
    print()
    return PB

def card_rank(card):
        rank_str = card.split()[0]  
        if rank_str == "J":
            return 11
        elif rank_str == "Q":
            return 12
        elif rank_str == "K":
            return 13
        elif rank_str == "A":
            return 14
        else:
            return int(rank_str)
        
def init_helper(card1, card2):
    print("Initalizing helper...")
    print("Note: Version 0.1 ignores OAP")
    
    C1 = card_rank(card1)
    C2 = card_rank(card2)
    
    if card1[-1] == card2[-1]:  
        SB = 2
    else:
        SB = 0
    
    OAP = 0
    HS = (C1 + C2) + SB + PB - OAP

    # Print results
    print("\n * * * * * * * * * * * * * * * * * * * * * \n")
    print(f"Your cards are: '{card1}' and '{card2}' ")
    print(f"C1: {C1}, C2: {C2}, SB: {SB}, PB: {PB}, OAP: {OAP}")
    print(f"* Your current Hand Strength (HS) is: {HS} \n")
    return C1, C2, SB, PB, OAP, HS

init_buyin()

# while all(stack >= 1 for stack in player_stacks):
for i in range(1):
    
    bool_buyin = str(input("Would anyone like to buy more chips? y/n: "))
    
    while bool_buyin != "y" and bool_buyin != "n":
        print("y Or n motherfucker. I will ask again nicely.")
        bool_buyin = str(input("Would anyone like to buy more chips? y/n: "))
        
    if bool_buyin == "y":
        i = int(input("Buyer's Player number: "))
        a = int(input("Player's Buying amount: "))
        buy_in(i, a)
        print(f"All players' stack sizes are now {player_stacks}")
    else:
        print("All players are ready")
        
    print(f"Player's stack sizes are: {player_stacks}")
    
    deck = init_deck()
    deal_cards(deck, num_players)
    PB = calculate_position()
    card1 = player_hands[0][0]  
    card2 = player_hands[0][1]  
    C1, C2, SB, PB, OAP, HS = init_helper(card1, card2)

    # print(player_hands)
    print(f"\n{len(deck)} cards remaining in deck.")


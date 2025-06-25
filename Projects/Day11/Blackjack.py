import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculatescore(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    sum_of_cards = sum(cards)
    return sum_of_cards

def compare(u_score, comp_score):
    if u_score == comp_score:
        return "Draw!"
    elif comp_score == 0:
        return "You lose, The opponent has the Black Jack"
    elif u_score == 0:
        return "Win! With a Blackjack!"
    elif u_score > 21:
        return"You went Over! You lose."
    elif comp_score > 21:
        return "opponent went over, You Win!"
    elif u_score > comp_score:
        return " You Win!"
    else:
        return " You lose "
    
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    computer_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculatescore(user_cards)
        computer_score = calculatescore(computer_cards)
        print(f"Your cards: {user_cards} Current Score: {user_score}")
        print(f"Computer's First Card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else :
            user_deal = input("Type 'y' to get another card or Type 'n' to pass: ").lower()
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculatescore(computer_cards)
        
    print(f"Your final hand: {user_cards} and Final Score: {user_score}")
    print(f"Computer final hand: {computer_cards} and Computer score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
    print("\n " * 20)
    play_game()

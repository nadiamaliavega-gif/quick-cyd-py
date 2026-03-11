import random
card_values = {'ace_1': 1, 'ace_11':11, 'two': 2, 'three': 3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':10,'queen':10,'king':10}

set_deck = ['ace','ace','ace','ace','two','two','two','two','three','three','three','three','four','four','four','four','five','five','five','five','six','six','six','six','seven','seven','seven','seven','eight','eight','eight','eight','nine','nine','nine','nine','ten','ten','ten','ten','jack','jack','jack','jack','queen','queen','queen','queen','king','king','king','king']

live_deck = []
live_deck += set_deck

hand = []
score = 0 
print('BlackJack')

card_fmt = (
    "┌─────────┐\n"
    "│{rank:<2}       │\n"
    "│         │\n"
    "│    {suit}    │\n"
    "│         │\n"
    "│       {rank:>2}│\n"
    "└─────────┘"
)
suits = ["♠", "♥", "♦", "♣"]
def show_card(card):
    suit = random.choice(suits)

    rank_map = {
        "ace": "A",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "ten": "10",
        "jack": "J",
        "queen": "Q",
        "king": "K"
    }
    rank = rank_map[card]
    print(card_fmt.format(rank=rank, suit=suit))

for i in range(2):
    card = live_deck[random.randint(0,len(live_deck)-1)]
hand.append(card)
live_deck.remove(card)
show_card(card)
if card == 'ace':
        print('you got an ace! one or eleven?')
        x = input()
        if x == 'one': card = 'ace_1'
        elif x == 'eleven': card = 'ace_11'
score += card_values[card]   
print('your hand',hand)
print('your score:',score)
print()
while score < 21:
    print('would you like to hit or stand?')
    x = input()
    print('you chose to'+ x)
    if x == 'hit':
       card = live_deck[random.randint(0,len(live_deck)-1)]
    hand.append(card)
    live_deck.remove(card)

show_card(card)
print('your hand',hand)
if card == 'ace':
            print('you got an ace! one or eleven?')
            x = input()
            if x == 'one': card = 'ace_1'
            elif x == 'eleven': card = 'ace_11'
score += card_values[card]

print('You stood, see if someone can beat',score)
if score == 21:
    print('woah you win')
else: print('you lose')
print('your score',score)
print()

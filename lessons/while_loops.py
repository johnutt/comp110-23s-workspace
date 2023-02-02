"""Demonstrates while loops by finding low value in string"""

cards: str = "5235"
low_card: int = int(cards[0])
card_idx: int = 0
#look at each number in string
while card_idx < 4:
    print(cards[card_idx])
    current_card: int = int(cards[card_idx])
    if (current_card < low_card):
        #update the low card
        low_card = current_card
    card_idx = card_idx + 1
print(low_card)
    

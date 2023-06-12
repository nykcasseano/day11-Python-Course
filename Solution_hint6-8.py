#Hint 6: Create a function called calculate_score() that takes a List of Cards as inputs
# And Returns the Score.
#Look up the sum() function to help you do this.
def calculate_score(cards):
    #Hint 7: Inside calculete_score() check for a blackjack (a hand with only 2 cards: ace + 10)
    #and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    #Hint 8: Inside caculate_score() check for an 11 (ace). If the score is alreadyover 21,
    # remove the 11 and replace it with a 1. You might need to look up append() and remove().
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

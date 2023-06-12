
#Hint 10: If the game has note ended, ask the user if they want to draw another card; If yes, then use the deal_card()
user_should_deal = input("Type 'y' to get another card, type 'n' to pass")
if user_should_deal == "y":
    user_cards.append(deal_card())
else:
    is_game_over = True
#function to add another card to the user_cars List. If no, then the game has ended.

#Hint 11: The score will need to be reachecked with every new card dreawn and the cheks in Hint 9 need to repeated until the game ends.

#Hint 12: Once the user is done and no longer wants to draw more cards, it's time to let the cumputer play. The computer wshould keep drawing cards as long as it has a score less than 17.

while computer_score !=0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    
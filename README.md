# Python-Blackjack-game

Introduction to Blackjack:

Blackjack, also known as 21, is a popular card game played in casinos around the world. The game is a comparing card game between one or more players and a dealer, where each player, in turn, competes against the dealer but does not play against other players. The primary objective of the game is to beat the dealer by having a hand value as close to 21 as possible without exceeding it.

Card Values:

Number cards (2-10) are worth their face value.
Face cards (Jack, Queen, King) are each worth 10 points.
Aces can be worth 1 or 11 points, depending on which value benefits the hand more.


# Method 1
This Python script is a simple program that simulates dealing cards from a deck of 52 playing cards. Here's an explanation of the code:

The script imports the random module to shuffle the deck of cards.
The cards list is created to store all the cards in the deck. It is populated with a list of lists, where each inner list contains a suit and a rank.
The suits list contains the four suits in a deck of cards: "Spades", "clubs", "hearts", and "diamonds".
The ranks list contains the 13 ranks in a deck of cards: "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", and "K".
The shuffle function shuffles the cards list using the random.shuffle function.
The deal function takes an integer number as an argument and deals that many cards from the cards list. It returns a list of the dealt cards.
The shuffle function is called to shuffle the deck of cards.
Four cards are dealt from the deck using the deal function and stored in the cards_dealt list.
The first card in the cards_dealt list is assigned to the card variable.
The rank of the card is extracted and stored in the rank variable.
An if-elif statement is used to determine the value of the card based on its rank. If the rank is "A", the value is set to 11. If the rank is "J", "Q", or "K", the value is set to 10. Otherwise, the value is set to the rank itself.
A dictionary rank_dict is created to store the rank and value of the card.
The rank and value of the card are printed using the print function.
Overall, this script demonstrates how to create a deck of cards, shuffle it, and deal a certain number of cards from it. It also shows how to determine the value of a card based on its rank.



# Method 2 
This Python script is a simple implementation of a deck of cards and a function to deal a certain number of cards from the deck. Here's an explanation of the code:

The script imports the random module to shuffle the deck of cards.
The cards list is initialized as an empty list.
The suits list contains the four suits of a deck of cards: "Spades", "clubs", "hearts", and "diamonds".
The ranks list contains dictionaries that represent the 13 ranks of a deck of cards. Each dictionary has two keys: "rank" and "value". The "rank" key contains the rank as a string, and the "value" key contains the rank's value as an integer.
A nested loop iterates over the suits and ranks lists, and for each combination, it appends a list containing the suit and rank to the cards list.
The cards list is shuffled using the random.shuffle function.
The shuffle function is defined to shuffle the cards list.
The deal function takes an integer number as an argument and returns a list of number cards dealt from the top of the cards list. The function uses a loop to pop number cards from the cards list and appends them to a new list cards_dealt. The function then returns the cards_dealt list.
The shuffle function is called to shuffle the cards list.
One card is dealt from the deck using the deal function and stored in the card variable.
The card variable is printed, which contains a list with two elements: the suit and rank of the dealt card.
Overall, this script demonstrates how to create a deck of cards, shuffle it, and deal cards from it. The script could be extended to deal multiple cards or to keep track of the remaining cards in the deck.


# Final Code 
This is a Python script for a simple text-based Blackjack game. The script defines several classes to represent the game's components, including Card, Deck, Hand, and Game. Here's a brief overview of each class:

Card: Represents a single playing card with a suit and a rank.
Deck: Represents a deck of playing cards, which can be shuffled and dealt.
Hand: Represents a hand of playing cards, which can be dealt, have cards added, and have their value calculated.
Game: Represents a Blackjack game, which can be played with a specified number of games.
The script also includes a check_winner function that determines the winner of a Blackjack game based on the values of the player's and dealer's hands.

The main part of the script creates a Game object and calls its play method to start the game. The play method prompts the user to enter the number of games to play, then plays each game by dealing two cards to both the player and the dealer, allowing the player to hit or stand, and determining the winner based on the final hand values.

Here's a more detailed breakdown of the script:

The Card class defines a __init__ method that takes a suit and rank and sets them as instance variables. It also defines a __str__ method that returns a string representation of the card.
The Deck class defines a __init__ method that creates an empty list of cards and initializes it with all 52 possible cards by iterating over a list of suits and ranks. It also defines a shuffle method that shuffles the list of cards using the random.shuffle function, and a deal method that deals a single card from the deck and removes it from the list.
The Hand class defines a __init__ method that creates an empty list of cards and initializes it with a value of 0 and a dealer flag. It also defines an add_card method that adds a list of cards to the hand, a calculate_value method that calculates the hand's value based on the ranks of the cards, and a get_value method that returns the hand's value. Additionally, it defines an is_blackjack method that checks if the hand's value is exactly 21, and a display method that prints the hand's cards and value.
The Game class defines a play method that prompts the user to enter the number of games to play, then plays each game by creating a new deck, dealing two cards to both the player and the dealer, and allowing the player to hit or stand until their hand value is 21 or higher. It then determines the winner based on the final hand values and prints the results. The check_winner function is called to determine the winner.
Overall, this script provides a simple text-based Blackjack game that can be played from the command line. It uses classes to represent the game's components and functions to determine the winner and handle user input.


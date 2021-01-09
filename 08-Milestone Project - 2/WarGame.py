import random

# SUIT, RANK, VALUE
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# CARD Class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
     
    def __str__(self):
        return self.rank + " of " + self.suit 


# DECK Class
class Deck:
    
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                #create cards
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)      
        
    def deal_one(self):
        return self.all_cards.pop()             

if __name__ == "__main__":
    
    #create some cards objects
    print("\n===========Card class object ===========")
    two_hearts = Card("Hearts", "Two")
    print(two_hearts)
    
    three_of_clubs = Card("Clubs", "Three")
    print(three_of_clubs)
    
    print(two_hearts.value < three_of_clubs.value)
    
    #create new deck object
    new_deck = Deck()
    
    first_card = new_deck.all_cards[0]
    last_card = new_deck.all_cards[-1]
    
    print("\n===========Deck class object ===========")
    print(first_card)
    print(last_card)
       
    new_deck.shuffle()    
    # print("\nDeck cards after shuffle:\n")
    # for card in new_deck.all_cards:
    #     print(card)
    
    print("Current deck length: " + str(len(new_deck.all_cards)))
    
    my_card = new_deck.deal_one()
    print(my_card)
    
    print("Current deck length: " + str(len(new_deck.all_cards)))
    

  
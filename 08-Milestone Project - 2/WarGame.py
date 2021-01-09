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
    

class Player:
    
    def __init__(self, name):
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0);
    
    def add_cards(self, cards):
        if type(cards)==type([]):
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)
            
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
        
    
def play_war_game():
    
    # Game setup
    player_one = Player("One")

    player_two = Player("Two")
    
    new_deck = Deck()
    new_deck.shuffle()
    
    for x in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())
    
    #print(player_one)
    #print(player_two)
    
    round_number = 0
    game_on = True  
    while game_on:  
        
        round_number += 1;    
        print(f'Round {round_number}')
        
        # check to see if a player is out of cards
        if len(player_one.all_cards) == 0:
            print('Player One, out of cards! Player Two wins')
            game_on = False
            break
        
        if len(player_two.all_cards) == 0:
            print('Player Two, out of cards! Player One wins')
            game_on = False
            break
        
            
        # Otherwise, the game is still on!
    
        # Start a new round and reset current cards "on the table"
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())
        
        player_two_cards = []
        player_two_cards.append(player_two.remove_one())
        
        # while at war
        at_war = True     
        while at_war:
            
            # Player Two Has higher Card
            if player_one_cards[-1].value < player_two_cards[-1].value:
                # player two get the cards
                player_two_cards.append(player_one_cards)
                player_two_cards.append(player_two_cards)
                
                # no longer at "war", time for next round 
                at_war = False
                break
            
            # Player One Has higher Card    
            elif player_one_cards[-1].value > player_two_cards[-1].value:
                
                # player two get the cards
                player_one_cards.append(player_one_cards)   
                player_one_cards.append(player_two_cards)  
                
                # no longer at "war", time for next round 
                at_war = False
                break    
            
            # Otherwise, we're still at war, so we'll add the next cards      
            else:
                print("WAR !!!")
                # This occurs when the cards are equal.
                # We'll grab another card each and continue the current war.
            
                # First check to see if player has enough cards
          
                # Check to see if a player is out of cards:
                if len(player_one.all_cards) < 3:
                    print("Player One unable to declare war")
                    print("Player Two WINS!!!!")
                    game_on = False
                    break
                elif len(player_two.all_cards) < 3:
                    print("Player Two unable to declare war")
                    print("Player One WINS!!!!")
                    game_on = False
                    break
                # Otherwise, we're still at war, so we'll add the next cards
                else:
                    for num in range(3):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())    
                
        
def testMyClasses():
    
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
    
    
    print("\n===========Player class object ===========")
    new_player = Player("Jose")
    my_card = Card("Spades", "Six")
    new_player.add_cards(my_card)
    new_player.add_cards([my_card, my_card, my_card, my_card])
    
    print(new_player)
    #print(new_player.all_cards[0])
    
    new_player.remove_one()
    print(new_player)
            
                 
if __name__ == "__main__":

    #play the war game
    play_war_game()
    
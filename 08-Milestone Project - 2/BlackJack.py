import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
     
    def __str__(self):
        return self.rank + " of " + self.suit + ' (' + str(self.value) + ')'
    
    
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                #create cards
                new_card = Card(suit, rank)
                self.deck.append(new_card)
    
    def __str__(self):
        deck_cards = ''
        for card in self.deck:
            deck_cards += '\n' + card.__str__()
        return deck_cards

    def shuffle(self):
        random.shuffle(self.deck)      
        
    def deal(self):
        return self.deck.pop()          
    

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):    
        if self.aces > 0 and self.value > 21:
            self.aces -=1
            self.value -=10
        
    def __str__(self):
        hand_cards = ''
        for card in self.cards:
            hand_cards += '\n' + card.__str__()
        return hand_cards
                    

class Chips:
 
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet            
        
    def __str__(self):
        return f'Total chips is {self.total} and bet {self.bet}'

#Step 6: Write a function for taking bets
def take_bet(chips):
    while True:    
        try:
            chips.bet = int(input("How many chips you you like to bet?\n"))
        except:
            print("Sorry, a bet must be an integer!")            
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break
                

#Step 7: Write a function for taking hits
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

#Step 8: Write a function prompting the Player to Hit or Stand
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break
    
#Step 9: Write functions to display cards
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

#Step 10: Write functions to handle end of game scenarios
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("\nPlayer wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("\nDealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("\nDealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("\nDealer and Player tie! It's a push.")

#And now on to the game!!
while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\nDealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
        
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())    
    
    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
       
        while dealer_hand.value <= player_hand.value or  dealer_hand.value < 17:
            hit(deck, dealer_hand)
        
        # Show all cards
        show_all(player_hand, dealer_hand) 
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand);
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    try_again = input("\nDo you want to play again ? Enter 'y' or 'n' \n")
    if try_again[0].lower() == 'y':
        playing = True
        continue
    elif try_again[0].lower() == 'n':
        print("Thank you for playing")
        playing = False
        break
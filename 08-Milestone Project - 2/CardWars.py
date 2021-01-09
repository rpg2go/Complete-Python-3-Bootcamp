# Attempted solution of Riddler at https://fivethirtyeight.com/features/riddler-nation-goes-to-war/

from random import shuffle

# Play the next cards and break any ties. Return True if
# there are more cards to play. 
def PlayContinues():
	global MyDeck,YourDeck,GameResult,CardsDown,Rep
	# The Pot is a list of all the cards at play in the round
	Pot = []
	while True:
		MyCard = MyDeck.pop()
		YourCard = YourDeck.pop()
		Pot.extend([MyCard,YourCard])
		shuffle(Pot)
		if MyCard > YourCard:
			MyDeck = Pot + MyDeck
			if len(YourDeck) == 0:
				# GameResult: 1 if win, 2 if I don't win, and 
				# 0 if game continues.
				GameResult = 1
			else:
				GameResult = 0
			break
		elif YourCard > MyCard:
			YourDeck = Pot + YourDeck
			if len(MyDeck) == 0:
				GameResult = 2
			else: 
				GameResult = 0
			break
		else:
			# A tie (war).
			if len(MyDeck) < 1 + CardsDown:
				# I don't have enough cards to play a tiebreak
				if len(YourDeck) < 1 + CardsDown:
					# And neither do you. Start the game from scratch.
					Rep -= 1
				GameResult = 2
				break
			elif len(YourDeck) < 1 + CardsDown:
				GameResult = 1
				break
			else:
				# Play the tie-break, by first laying down the face-down
				# cards and then continuing the "while True" loop
				for _ in range(CardsDown):
					Pot.extend([MyDeck.pop(),YourDeck.pop()])
	return (GameResult == 0)

# You have four of every number from 0 to 11, while I have just four 12s

# Global parameters

# Ten million reps take less than ten minutes when this
# is run with PyPy (much faster than stock Python).
Reps = 1000000

# How many cards go face-down in a tie-break?
CardsDown = 1

# Main loop

YourCards = [n/4 for n in range(48)] 

# For normal, fair-deal War uncomment the next line.
#Deck = [n/4 for n in range(52)]

MyWins = 0
GamesWithNRounds = [0]*8000
LengthAccum = 0
for Rep in range(Reps):
	MyDeck = [12]*4
	shuffle(MyDeck)
	YourDeck = list(YourCards)
	shuffle(YourDeck)
	# For normal, fair-deal War, comment the previous three
	# and uncomment next three lines.
#	shuffle(Deck)
#	MyDeck = Deck[:26]
#	YourDeck = Deck[26:]
	Rounds = 1
	while PlayContinues():
		Rounds += 1
	GamesWithNRounds[Rounds] += 1
	LengthAccum += Rounds
	if GameResult == 1:
		MyWins += 1
print ("WinRate, GameLength:", 1.0*MyWins/Reps, 1.0*LengthAccum/Reps)
# Uncomment below for plottable list of frequencies of round lengths
#for i in range(1,4000):
#	print 1.0*GamesWithNRounds[i]/Reps
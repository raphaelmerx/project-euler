

def n_slices(n, list_):
    for i in xrange(len(list_) + 1 - n):
        yield list_[i:i+n]

def isSublist(sub_list, list_):
    for slice_ in n_slices(len(sub_list), list_):
        if slice_ == sub_list:
            return True
    return False

'''
read the line
get hand1, hand2
essayer les fonctions sur hand1, hand2
retourner best1, best2 formes d'un index et une list de cartes
comparer les index
si egaux, comparer les cartes
'''



# All functions will return a set with a boolean and when necessary, a list of values
# list of values will contain first the most important cards, etc
# e.g. if the hand is a pair, the pair will be given first
def isRoyalFlush(hand):
	values = []
	# get the color of the first card
	color = hand[1][1:2]
	for card in hand:
		if card[1:2] == color:
			values.append(card[0:1])
		else:
			return False
	return ( sorted(values) == sorted(['T','J','Q','K','A']) )

# Straight Flush: All cards are consecutive values of same suit.
def isStraightFlush(hand):
	values = []
	# Do cards all have the same suit?
	color = hand[1][1:2]
	for card in hand:
		if card[1:2] == color:
			values.append(card[0:1])
		else:
			return False
	# sorting according to the rules
	values = sorted(values, key= lambda figure: orderOfCards.index(figure))
	return ( isSublist(values,orderOfCards), values )

def isFourOfAKind(hand):
	# get the values
	values = []
	for card in hand:
		values.append(card[0:1])
	for value in values:
		if values.count(value)==4:
			lastValue = filter(lambda a: a != value, values)[0]
			return (True, [value, value, value, value, lastValue]  )
	return False

def isFullHouse(hand):
	# get the values
	values = []
	for card in hand:
		values.append(card[0:1])
	hasFull,hasPair = False, False
	for value in values:
		if values.count(value)==3:
			hasFull = True
			value1 = value
		if values.count(value)==2:
			hasPair = True
			value2 = value
	if hasFull and hasPair:
		return (True, [value1,value1,value1,value2,value2])
	else:
		return False

def isFlush(hand):
	suits = set()
	for card in hand:
		suits.add(card[1:2])
	if len(suits) == 1:
		values = sorted(values, key= lambda figure: orderOfCards.index(figure))
		return (True, values)
	else:
		return False

#Straight: All cards are consecutive values.
def isStraight(hand):
	values = []
	for card in hand:
		values.append(card[0:1])
	# sorting according to the rules
	values = sorted(values, key= lambda figure: orderOfCards.index(figure))
	if isSublist(values,orderOfCards):
		return (True, values)
	else:
		return False

# Three of a Kind: Three cards of the same value.
def isThreeOfAKind(hand):
	# get the values
	values = []
	for card in hand:
		values.append(card[0:1])
	for value in values:
		if values.count(value)==3:
			allButValue = filter(lambda a: a != value, values)
			allButValue = sorted(allButValue, key= lambda figure: orderOfCards.index(figure))
			return (True, [value, value, value] + allButValue )
	return False

# Two Pairs: Two different pairs.
def isTwoPairs(hand):
	# get the values
	values = []
	for card in hand:
		values.append(card[0:1])
	nbOfPairs = 0
	for value in values:
		if values.count(value)==2:
			nbOfPairs += 1
			values = filter(lambda a: a != value, values)
	loneCard = values[0]
	# recreate values from scratch
	values = []
	for card in hand:
		values.append(card[0:1])
	# keep only the two pairs
	values = filter(lambda a: a != loneCard, values)
	values = sorted(values, key= lambda figure: orderOfCards.index(figure)) 
	if nbOfPairs == 2:
		return (True, values + [loneCard])
	else:
		return False

# One Pair: Two cards of the same value.
def isOnePair(hand):
	# get the values
	values = []
	for card in hand:
		values.append(card[0:1])
	nbOfPairs = 0
	for value in values:
		if values.count(value)==2:
			nbOfPairs += 1
			pairValue = value
			values = filter(lambda a: a != value, values)
	values = sorted(values, key= lambda figure: orderOfCards.index(figure)) 
	if nbOfPairs == 1:
		return (True, [pairValue, pairValue] + values)
	else:
		return False

def highestCard(hand):
	# get the values
	values = []
	for card in hand:
		values.append(card[0:1])
	values = sorted(values, key= lambda figure: orderOfCards.index(figure)) 
	return (True, values)

orderOfCards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
orderOfHands = [isRoyalFlush, isStraightFlush, isFourOfAKind, isFullHouse, isFlush, isStraight,
isThreeOfAKind,isTwoPairs, isOnePair, highestCard]

def getHandValue(hand):
	for func in orderOfHands:
		if func(hand) != False:
			best = orderOfHands.index(func)
			return (best, func(hand)[1])

f = open('pb_54_data.txt', 'r')

# 1000 lines is ok for memory
allHands = f.readlines()
player1Wins = 0
for oneRound in allHands:
	hand1, hand2 = [],[]
	for i in range(5):
		hand1.append(oneRound[3*i:3*i+2])
	for i in range(5,10):
		hand2.append(oneRound[3*i:3*i+2])
	best1 = getHandValue(hand1)
	best2 = getHandValue(hand2)
	if best1[0] < best2[0]:
		player1Wins += 1
	elif best1[0] == best2[0]:
		hand1 = best1[1]
		hand2 = best2[1]
		win1 = False
		i = 0
		while win1 == False and i<5:
			index1 = orderOfCards.index(hand1[i])
			index2 = orderOfCards.index(hand2[i])
			if index1 < index2:
				win1 = True
				player1Wins += 1
			elif index1 > index2:
				break
			i = i+1


	# hand1, hand2 lists of the cards in the hands of players

		

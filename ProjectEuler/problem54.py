
cards = "5H 3C 3S 3S 2D 9C TS JS QD KD"
#cards = "9H JH QH KH AH 2C 3S 8S 8D TD"



values = {
	'2' : 0,
	'3' : 1,
	'4' : 2,
	'5' : 3,
	'6' : 4,
	'7' : 5,
	'8' : 6,
	'9' : 7,
	'T' : 8,
	'J' : 9,
	'Q' : 10,
	'K' : 11,
	'A' : 12
}

def high_card(h):
	return values[str(h[-1][0])]

def card_counter(h):
	cards = {}
	for c in h:
		if not values[str(c[0])] in cards.keys():
			cards[values[str(c[0])]] = 1
		else:
			cards[values[str(c[0])]] += 1
	return cards

def royal_straight_and_or_flush(h):
	straight = True
	flush = True
	royal = True
	ace_straight = False

	if h[4][0] == 'A':
		ace_straight = True

	suit = h[0][1]
	start_value = values[str(h[0][0])]

	if start_value != 8:
		royal = False
	for c in h:
		if c[1] != suit:
			flush = False
		if values[str(c[0])] != start_value:
			straight = False
		else:
			start_value += 1

	if ace_straight and not straight:
		#print("Ace Straight Check: ",h)
		start_value = 0
		straight = True
		for c in h[:-1]:
			if values[str(c[0])] != start_value:
				straight = False
			else:
				start_value += 1

	return (straight,flush,royal)

def scorer(outcomes): 
	p1 = list(outcomes[0].items())
	p2 = list(outcomes[1].items())
	#print(p1,p2)
	for i in range(len(outcomes[0].items())):
		index = len(outcomes[0].items()) - i - 1
		if p1[index][1] != 0 or p2[index][1] != 0: # If a Hand is detected
			if p1[index][1] == 0 or p2[index][1] == 0: # If one has a Hand while the other doesnt,
				return p1[index][1] != 0			   # then they win by default
			try:	# else
				if (p1[index][1] == p2[index][1]): # Tiebreaker High Card
					return p1[0][1] < p2[0][1]
				else:
					return p1[index][1] < p2[index][1]
			except TypeError: # For handling full house hands vs non-full house hands
				return p1[index][1] != 0
		

					
 

file = open("problem54(poker_hands).txt","r")
p1_wins = 0
while True:
	cards = file.readline()
	if not cards:
		break
	hands = [cards[:14],cards[15:]]
	hands = [h.split(" ") for h in hands]
	hands = [[(c[0],c[1]) for c in h] for h in hands]

	outcome = []
	for hand in hands:
		#print(hand)
		potential_outcomes = {
			"High Card" : 0,
			"One Pair" : 0,
			"Two Pair" : 0,
			"Three of a Kind" : 0,
			"Straight" : 0,
			"Flush" : 0,
			"Full House" : 0,
			"Four of a Kind" : 0,
			"Straight Flush" : 0,
			"Royal Flush" : 0
		}

		hand = sorted(hand, key=lambda card: values[str(card[0])])

		potential_outcomes["High Card"] = high_card(hand)
		card_count = card_counter(hand).items()
		for i in card_count:
			if i[1] == 2:
				potential_outcomes["One Pair"] = i[0]
				for k in card_count:
					if k[1] == 2 and i[0] != k[0]:
						potential_outcomes["Two Pair"] = (i[0],k[0])
			if i[1]	== 3:
				potential_outcomes["Three of a Kind"] = i[0]
				for k in card_count:
					if k[1] == 2:
						potential_outcomes["Full House"] = (i[0],k[0])
			if i[1] == 4:
				potential_outcomes["Four of a Kind"] = i[0]

		sfr = royal_straight_and_or_flush(hand)
		if sfr[0] and sfr[1] and sfr[2]:
			potential_outcomes["Royal Flush"] = 12
		else:
			if sfr[0] and sfr[1]:
				potential_outcomes["Straight Flush"] = values[str(hand[-1][0])]
			else:
				if sfr[0]:
					potential_outcomes["Straight"] = values[str(hand[-1][0])]
				if sfr[1]:
					potential_outcomes["Flush"] = values[str(hand[-1][0])]

		outcome.append(potential_outcomes.copy())

	if not scorer(outcome):
		p1_wins += 1
print(p1_wins)

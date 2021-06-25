import numpy as np

#PARAMS
basic_deck = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]; #['A', '10', '10', '10', '10', '9', '8', '7', '6', '5', '4', '3', '2'];
number_of_decks = 1;
number_of_hands = 2; #W/o Dealer
init_bankroll = 1000;
SOFT_17 = True;

def shuffle_hand(number_of_decks):
	shuffled_deck = [];

	for i in range(len(basic_deck)):
		for j in range(number_of_decks):
			for k in range(4):
				shuffled_deck.append(basic_deck[i]);


	np.random.shuffle(shuffled_deck)
	return shuffled_deck;

def deal_hand(deck, num_players):
	cards_pulled_from_deck = [];
	dealt_hands = [];

	if(len(deck) < (num_players+1)*2):
		print('ERR: Need new deck')
	else:
		# Take Cards ffrom Deck and put them in hand
		for i in range((num_players+1)*2): cards_pulled_from_deck.append(deck[0]); deck.pop(0);

		# Arrange Players' Hand
		for i in range(num_players+1): dealt_hands.append([cards_pulled_from_deck[i], cards_pulled_from_deck[i+num_players+1]]);

	return deck, dealt_hands;

def execute_dealer_Action(deck, hand):
	hand.sort();
	# Check 21
	if(sum(hand) == 21): print('DEALER BLACKJACK'); return hand, 21;
	# Pair of Aces
	if(hand[0] == 11 and hand[1] == 11): hand[0] = 1;

	if(SOFT_17):
		while(sum(hand) < 17): #Stand on soft 17
			hand.append(deck[0]); print('New Dealt Card: ', deck[0]); deck.pop(0); hand.sort();

			# If soft ace puts above 21
			if(sum(hand) > 21): 
				if(hand[(len(hand)-1)] == 11): hand[(len(hand)-1)] = 1; hand.sort();
				else: return hand, sum(hand);
			print('Hand Sum: ', sum(hand))
	else: print("ERROR")

	return hand, sum(hand);

def execute_basic_strategy(deck, dealer_card, hand):
	#Check 21
	if(sum(hand) == 21): print('PLAYER BLACKJACK'); return hand, 21;

	#Check Split
	if(hand[0] == hand[1]): hand = hand_splitting(deck, dealer_card, hand);



	# Do WE Split?
	#if(hand[0] == hand[1]): hand_splitting(deck, dealer_card, hand);
	return hand;

def hand_splitting(deck, dealer_card, hand):
	print('Checking Split Options:')
	new_hand = [];
	if(hand[0] == 11):
		new_hand.append([11, deck[0]]); deck.pop(0); new_hand[0].sort();
		new_hand.append([11, deck[0]]); deck.pop(0); new_hand[1].sort();
		return new_hand;
	elif(hand[0] == 10): return [10, 10];
	elif(hand[0] == 9): 
		if(dealer_card == 7 or dealer_card >= 10 or dealer_card == 1): return [9,9];
		else:
			new_hand.append([9, deck[0]]); deck.pop(0); new_hand[0].sort();
			new_hand.append([9, deck[0]]); deck.pop(0); new_hand[1].sort();
			return new_hand;
	elif(hand[0] == 8):
		new_hand.append([8, deck[0]]); deck.pop(0); new_hand[0].sort();
		new_hand.append([8, deck[0]]); deck.pop(0); new_hand[1].sort();
		return new_hand;
	elif(hand[0] == 7):
		if(dealer_card >= 9): return [7,7];
		else:	
			new_hand.append([7, deck[0]]); deck.pop(0); new_hand[0].sort();
			new_hand.append([7, deck[0]]); deck.pop(0); new_hand[1].sort();
			return new_hand;
	elif(hand[0] == 6):
		if(dealer_card >= 8): return [6,6];
		else:	
			new_hand.append(6); new_hand.append([deck[0]]); deck.pop(0); new_hand[0].sort();
			new_hand.append(6); new_hand.append([deck[0]]); deck.pop(0); new_hand[1].sort();
			return new_hand;
	elif(hand[0] == 5): return [5,5];
	elif(hand[0] == 4):
		if(dealer_card == 5):
			new_hand.append(4); new_hand.append([deck[0]]); deck.pop(0); new_hand[0].sort();
			new_hand.append(4); new_hand.append([deck[0]]); deck.pop(0); new_hand[1].sort();
			return new_hand;
		else: return [4,4];
	elif(hand[0] == 3):
		if(dealer_card < 8):
			new_hand.append(3); new_hand.append([deck[0]]); deck.pop(0); new_hand[0].sort();
			new_hand.append(3); new_hand.append([deck[0]]); deck.pop(0); new_hand[1].sort();
			return new_hand;
		else: return [3,3];
	else:
		if(dealer_card < 8):
			new_hand.append(2); new_hand.append([deck[0]]); deck.pop(0); new_hand[0].sort();
			new_hand.append(2); new_hand.append([deck[0]]); deck.pop(0); new_hand[1].sort();
			return new_hand;
		else: return [2,2]; 


# Main Method
shuffled_deck = shuffle_hand(number_of_decks)
print('Shuffled Deck: ', shuffled_deck)

deck, dealt_hands = deal_hand(shuffled_deck, number_of_hands);
print('Dealt Hands: ', dealt_hands)

#Execute Games
for i in range(number_of_hands):
	print('Hand Index: ', i+1)
	#execute_basic_strategy(deck, dealt_hands[0][0], dealt_hands[i+1]);

print('HERE:')
hand = execute_basic_strategy(deck, 7, [8,8]);
print('NEW HAND: ', hand)


hand, value = execute_dealer_Action(deck, dealt_hands[0]);
print('Hand: ', hand); print('Hand Value: ', value); 

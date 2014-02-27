import random
# Ben
print """Welcome to the war game of the ages! This is War, by Elliot, Ethan, Austin, and Ben!
War is a card game in which two cards from seperate, random, decks are drawn and pitted against each other.
The goal of War is to have the higher card of the pair.
If the same rank is drawn, both players will draw three more cards, placed face down, and reveal them one at a time to eachother
Whoever has the highest combination of the pairs wins the battle, and the cards.
At the end, whoever has the most cards wins the game, and bragging rights."""
# Elliot
BOTTOM, RANDOM = 'bottom', 'random'
 
class Card(object):
	"""docstring for Card"""
	def __init__(self, _rank, _suit, _rankname, _suitname):
		self._rank = _rank
		self._suit = _suit
		self._rankname = _rankname
		self._suitname = _suitname
		
	def getSuit(self):
		return self._suit
		
	def getRank(self):
		return self._rank
		
	def setSuit(self, suit):
		self._suit = suit
		
	def setRank(self, rank):
		self._rank = rank
		
	def __str__(self):
		return "%s of %s" % (self._rankname, self._suitname)
 
	def __cmp__(self,other):
		if self._rank < other._rank:
			return -1
		if self._rank > other._rank:
			return 1
		return 0		
 
class Hand(list):
	def add(self,card):
		"put a card on top of the deck"
		self.append(card)
 
	def push(self, card):
		"put a card on the bottom of the deck"
		self.reverse()
		self.append(card)
		self.reverse()
	
	# Elliot	
	def containsRank(self, rankname):
		"return True if the hand contains any card with this rankname"
		return any([rankname==i._rankname for i in self])
		
	# Ethan
	def removeCardByRank(self, rankname):
		"remove ONE card that has this rankname, else return False"
		for i in range(len(self)):
			if self[i]._rankname == rankname:
				return self.pop(i)
		return False


		
	
# Elliot
class Deck(Hand):
	"""docstring for Deck"""
	def __init__(self, ranks=None, suits=None):
		self.ranks = ranks or [
		"Two", "Three", "Four", "Five",
		"Six", "Seven", "Eight", "Nine", "Ten",
		"Jack", "Queen", "King", "Ace"]
		self.suits = suits or [
		"Clubs", "Diamonds", "Hearts", "Spades"
		]
		for rank, rankname in enumerate(self.ranks):
			for suit, suitname in enumerate(self.suits):
				self.append(Card(rank,suit,rankname,suitname))
 
 
 
	def draw(self, which=None):
		"draw the top card ( removes that card )"
		try:
			which = which.lower()
			if which == 'bottom':
				return self.pop(0)
			if which == 'random':
				return self.pop(random.randint(0,len(self)-1))
			return self.pop()
		except:
			return self.pop()
			
 
	def shuffle(self):
		"shuffle the deck"
		for i in range(7):
			random.shuffle(self)
 
	def cut(self):
		"split the deck in two and put the top half ( about half ) on the bottom"
		deck_length = len(self)
		start = deck_length/4
		end = deck_length - start
		cuthere = random.randint(start, end)
		newdeck = self[cuthere:] + self[:cuthere]
		self = newdeck

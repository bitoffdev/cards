import cards

class War(object):
	
	def __init__(self):
		self.roundCount = 0
		self.warCount = 0
		d = cards.Deck()
		d.shuffle()
		self.p1 = cards.Hand()
		self.p2 = cards.Hand()
		
		for i in range(len(d)):
			if i%2: self.p1.add(d.draw())
			else: self.p2.add(d.draw())
			
	def play(self):
		self.roundCount += 1
		#Draw cards
		if len(self.p1)>0:
			a = self.p1.pop()
		else:
			return 'P2 won! It took %i rounds. There were %i wars.' %(self.roundCount, self.warCount)
		if len(self.p2)>0:
			b = self.p2.pop()
		else:
			return 'P1 won! It took %i rounds. There were %i wars.' %(self.roundCount, self.warCount)
		#Compare cards
		if a > b:
			self.p1.add(a)
			self.p1.add(b)
		elif a < b:
			self.p2.add(a)
			self.p2.add(b)
		else:
			#war
			a_war = []
			b_war = []
			while True:
				#check for winner
				if len(self.p1) == 0:
					return 'P2 won! It took %i rounds. There were %i wars.' %(self.roundCount, self.warCount)
				elif len(self.p2) == 0:
					return 'P1 won! It took %i rounds. There were %i wars.' %(self.roundCount, self.warCount)
				#Increase warCount
				self.warCount += 1
				#Draw cards
				for i in range(min(4, len(self.p1))):
					a_war.append(self.p1.pop())
				for i in range(min(4, len(self.p2))):
					b_war.append(self.p2.pop())
				#Compare cards
				if a_war[-1] > b_war[-1]:
					for card in a_war: self.p1.add(card)
					for card in b_war: self.p1.add(card)
					break
				elif a_war[-1] < b_war[-1]:
					for card in a_war: self.p2.add(card)
					for card in b_war: self.p2.add(card)
					break
		return self.play()
		
if __name__ == "__main__":
	print War().play()

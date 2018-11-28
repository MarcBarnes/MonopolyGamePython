class Jail(object, Player, Dice):
	def __init__(self, Player p):
		self.d = Dice()
		self.counter = 0

	def leaveJailTest(self)
		while counter < 3:
			d.rollDice()
			if d.doubleChecker:
				p.moveSpaces(d.total)
			elif p.hasCard("getOutOfJailFree"):
				p.moveSpaces(1)
			elif p.bank > 50 and p.pay(50):
				d.rollDice()
				p.moveSpaces(d.total)
			else:
				counter += 1
		if counter == 3:
			p.pay(50)
			p.moveSpaces(d.total)

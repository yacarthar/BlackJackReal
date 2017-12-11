import random

#variable
diamonds= ['joker','A diamonds','2 diamonds','3 diamonds','4 diamonds','5 diamonds','6 diamonds','7 diamonds','8 diamonds','9 diamonds','10 diamonds','J diamonds','Q diamonds','K diamonds']
hearts= ['joker','A hearts','2 hearts','3 hearts','4 hearts','5 hearts','6 hearts','7 hearts','8 hearts','9 hearts','10 hearts','J hearts','Q hearts','K hearts']
clubs= ['joker','A clubs','2 clubs','3 clubs','4 clubs','5 clubs','6 clubs','7 clubs','8 clubs','9 clubs','10 clubs','J clubs','Q clubs','K clubs']
spades= ['joker','A spades','2 spades','3 spades','4 spades','5 spades','6 spades','7 spades','8 spades','9 spades','10 spades','J spades','Q spades','K spades']
fullDeck= [diamonds, hearts, clubs, spades]

pointDict1= {'':0,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':1}
pointDict2= {'':0,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
originalBallance= 2000

class Player():
	"""docstring for Player"""
	def __init__(self, ballance):
		self.name= 'player'
		self.money= ballance
		self.deck= ['x']*5
		self.point= 0
		self.bet= 0

	def changeMoney(self,num):
		self.money+= num
	def changeDeck(self,step):
		j= self.deck.index('x')
		for i in range(j,j+step):
			self.deck[i]= fullDeck[random.randint(0,3)][random.randint(1,13)]
		self.point = getPoint(self.deck)
	def reset(self):
		self.deck= ['x']*5
		self.point= 0


def clearType(str):
	j=str.find(' ')
	return str[:j]
def getPoint(deck):
	
	if deck.count('A') + deck.count('x') ==5:
		s= deck.count('A')
	else:
		s=0
		for i in deck:
			s+= pointDict1[clearType(i)]
		if s==21 and deck.count('x')==3:
			pass	
		elif s<11: 
			s=0
			for i in deck:
				s+= pointDict2[clearType(i)]
	return s

class Dealer():
	"""docstring for Dealer"""
	def __init__(self):
		self.name= 'dealer'
		self.deck= ['x']*5
		self.point = 0
	def changeDeck(self,step):
		j= self.deck.index('x')
		for i in range(j,j+step):
			self.deck[i]= fullDeck[random.randint(0,3)][random.randint(1,13)]
		self.point = getPoint(self.deck)
	def reset(self):
		self.deck= ['x']*5
		self.point= 0
p= Player(2000)
d= Dealer()
player= p
dealer= d

def showCard1():
	print ("player's Card: %s %s %s %s %s  ------ %d" %(player.deck[0],player.deck[1],player.deck[2],player.deck[3],player.deck[4], player.point))
	print ("dealer's Card: %s ## %s %s %s  ------ " %(dealer.deck[0],dealer.deck[2],dealer.deck[3],dealer.deck[4] ))
def showCardEnd():
	print ("player's Card: %s %s %s %s %s  ------ point %d" %(player.deck[0],player.deck[1],player.deck[2],player.deck[3],player.deck[4], player.point))
	print ("dealer's Card: %s %s %s %s %s  ------ point %d" %(dealer.deck[0],dealer.deck[1],dealer.deck[2],dealer.deck[3],dealer.deck[4], dealer.point ))
	print ('player Money: %d' %player.money)

def showOption1():
	print ('press d to Double')
	print ('press h to hit')
	print ('press s to surrender')
	print ('press n to stand')
def showOption2():
	print ('press h to hit')
	print ('press n to stand')

def blackjackCheck(turn):
	if turn.point == 21 and (clearType(turn.deck[0])== 'A' or clearType(turn.deck[1])== 'A' ) and ('10' not in turn.deck[0]) and ('10' not in turn.deck[1]) :
		return True
def busted(turn):
	return turn.point >21


def newGame():
	
	#player turn
	print ('------------------------')
	print ('MONEY :        %d' %player.money)
	player.bet= int(input('\n how much would you like to bet?? :  '))
	player.changeDeck(2)
	dealer.changeDeck(2)
	showCard1()
	if blackjackCheck(player):
		print (player.name +' get BLACKJACK, you WIN')
		
	showOption1()
	chooseOption= input()
	if chooseOption=='d':
		player.changeDeck(1)
		wincheck()
	elif chooseOption=='h':
		hit()
	elif chooseOption=='s':
		surrender()
	elif chooseOption=='n':
		stand()

		


def wincheck():
	if player.point > dealer.point:
		player.money+=player.bet
		print ('player point: %d --dealer point: %d'%(player.point, dealer.point))
		print ('player win')
		print ('player Money: %d' %player.money)
	elif player.point < dealer.point:
		player.money-= player.bet
		print ('player point: %d --dealer point: %d'%(player.point, dealer.point))
		print ('player lose')
		print ('player Money: %d' %player.money)
	else:
		print ('player point: %d --dealer point: %d'%(player.point, dealer.point))
		print ('DRAW')
		print ('player Money: %d' %player.money)
	 


def hit():
	while True:
		player.changeDeck(1)
		showCard1()
		if not busted(player):
			showOption2()
			chooseOption = input()
			if chooseOption =='h':
				continue
			if chooseOption =='n':
				stand()
				break
		else:
			player.money-=player.bet
			print ('player point: %d --dealer point: %d'%(player.point, dealer.point))
			print ('>>>>>>>>>>> player BUSTED')
			print ('player Money: %d' %player.money)
			break


def stand():
	dealerTurn()
	if busted(dealer):
		player.money +=player.bet
		showCardEnd()
		print ('>>>>>>>>>>>>> player WIN - dealer BUSTED')
	else:
		wincheck()

def surrender():
	showCardend()
	player.money-= player.bet/2
	showCardend
	print ('>>>>>>>>>>>  player lose')

def dealerTurn():
	while dealer.point <17:
		dealer.changeDeck(1)


#MAIN
while True:
	print ('------------------------------------------------------------------')
	print ('Welcome to LAS VEGAS                      Money:  %d'%player.money)
	print ('press 1 to continue with current ballance')
	print ('press 2 to start a new game')
	print ('press 3 to exit')
	choose= int(input('press here to make decision \n'))
	if choose ==2:
		# player= p
		# dealer= d
		player.money= 2000
		newGame()
		player.reset()
		dealer.reset()
	if choose ==1:
		player.reset()
		dealer.reset()
		if player.money <=0:
			print ("you're out of money, pls select 'NEW GAME'")	
		else:
			newGame()
	if choose ==3:
		print ('GOOD BYE')
		break
		

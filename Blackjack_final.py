import random
class Cards:
    
    def __init__(self):
        self.suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        self.ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        self.values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
       
        pass
    
    def __str__(self):
        pass



class Deck(Cards):
    
    def __init__(self):
        Cards.__init__(self)
        self.deck = []  # start with an empty 
        self.value = {}
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(f'{suit} {rank}')
                self.value.update({f'{suit} {rank}':self.values[rank]})
                pass
                
        self.num = -1
    def __str__(self):
        return "test"
        pass

    def shuffle(self):
        random.shuffle(self.deck)

        
    def deal(self):
        self.num = self.num + 1
        return self.deck[self.num]
        
        pass



class Chips():
    
    def __init__(self,total,bet):
        
        #Deck.__init__(self)
        self.total = total
        self.bet = bet
        
    def win_bet(self):
        self.total = self.total + self.bet
        print(f'You won, you know have {self.total}')
        pass
    
    def lose_bet(self):
        self.total = self.total - self.bet
        print(f'You lost, you know have {self.total}')
        pass

    def __str__(self):
        return f'You are betting {bet}'
        pass


def take_bet():

    bet = input("How much would you like to bet")
    return int(bet)
    
def hits(dealed_cards,cards_values,i):
        dealed_cards.append(game.deal())
        print(f'{dealed_cards} ')
        cards_values = cards_values + game.value[dealed_cards[i]]
        print(f'total value: {cards_values} \n')
        return cards_values
        #i = i + 1
        #playing = evaluate(Pcards_values)
        pass

def initial_hit(dealed_cards):
    dealed_cards.append(game.deal())
    dealed_cards.append(game.deal())

    print(f'cards : {dealed_cards[0]} and {dealed_cards[1]} ')
    cards_values = game.value[dealed_cards[0]] + game.value[dealed_cards[1]]
    print(f'total value: {cards_values} \n')
    return cards_values


def Pevaluate(Total_value):
    if Total_value == 21:
        print('!!!!!!WIN!!!!!!')
        return False
    if Total_value > 21:
        print('!!!!!!BUST!!!!!!')
        return False
    else:
        return True
        pass

def Devaluate(Total_value):
    if Total_value > 21:
        #print('!!!!!!BUST!!!!!!')
        return False
    if Total_value == 17 or Total_value > 17:
        #print('Dealer play is over')
        return False
    else:
        return True
        pass









global playing
playing = True
D_playing = True
game_mode = True
#global Pdealed_cards 
Pdealed_cards = []
#global Ddealed_cards 
Ddealed_cards = []
i = 2

#####Error handeling >>
while True:
    try:
        total = int(input("How much money do you have?"))
    except ValueError: #If user input non-integer value
        print("Value error!!")
    else: #If user input an integer value, break out of the loop
        break

    
bet = take_bet()

player = Chips(total, bet)


game_mode = True



while game_mode == True:
    playing = True
    D_playing = True
    
    #global Pdealed_cards 
    Pdealed_cards = []
    #global Ddealed_cards 
    Ddealed_cards = []
    i = 2

    game = Deck()

    game.shuffle()

    print('\n~~~~~~Player:')
    Pcards_values = initial_hit(Pdealed_cards)

    print('~~~~~~Dealer:')
    Dcards_values = initial_hit(Ddealed_cards)
    #bet = take_bet()
    skip = False
    while playing == True: 
        
        hit = input("Would you like to hit? y or n")
        if hit == 'n':
            playing = False
        if hit == 'y':

            #Player hitting
            print("\n \n \n \n \n~~~~~~Player:")
            Pcards_values = hits(Pdealed_cards,Pcards_values,i)
            playing = Pevaluate(Pcards_values)
            i = i + 1
            if Pcards_values > 21:
                skip = True
            

    i = 2
    while D_playing == True and skip == False: 
        #Dealer hitting:
        print("\n \n \n \n ~~~~~~Dealer:") 
        Dcards_values = hits(Ddealed_cards,Dcards_values,i)
        D_playing = Devaluate(Dcards_values)

        i = i + 1

    
    if (Pcards_values > Dcards_values or Dcards_values > 21) and ( (Pcards_values <= 21 or Dcards_values > 21) and Dcards_values != 21 ) : 
        player.win_bet()
        play_again = input("Would you like to play again? y or n")
    if (Pcards_values < Dcards_values and Dcards_values <= 21 ) or Pcards_values > 21: 
        player.lose_bet()
        play_again = input("Would you like to play again? y or n")

    if Pcards_values == Dcards_values:
        print("!!!!!!TIE!!!!!!")
        play_again = input("Would you like to play again? y or n")


    if play_again == 'n': game_mode = False
        


#######When player busted. dealer dont need to play. Auto lose. 8/31/2020
        #player.shuffle()

    #dealed_card = player.deal(num)

    #print(dealed_card)


    #player = Deck()
    #print(player)

    #print(player.deck)

    #player.shuffle()
    #card = player.deck[2]
    #print(card)
    #print("\n")

    #print(player.value[card])







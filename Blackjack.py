
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
        self.deck = []  # start with an empty list
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(f'{suit} {rank}')
                pass
    
    def __str__(self):
        pass

    def shuffle(self):
        pass
        
    def deal(self):
        pass

player = Deck()
print(player.deck)
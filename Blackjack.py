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
        
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(f'{suit} {rank}')
                pass
    
    def __str__(self):
        return "test"
        pass

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return deck[i]
        pass

player = Deck()
print(player)

print(player.deck)
#player.shuffle()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):

        pass
    
    def adjust_for_ace(self):
        pass


 
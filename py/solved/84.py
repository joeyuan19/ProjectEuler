import random

class CardDeck(object):
    def __init__(self,cards):
        self.deck = cards
        random.shuffle(self.deck)

    def draw(self):
        card = self.deck.pop()
        self.deck.insert(0,card)
        return card

class Die(object):
    def __init__(self,sides):
        self.sides = sides

    def roll(self):
        return random.randint(1,self.sides)

class Board(object):
    def __init__(self):
        self.hist = [0]*40
        self.position = 0
        self.dice = (Die(6),Die(6))
        self.chance = CardDeck([
            '','','','',
            '','','10','rail',
            'rail','util','-3','0',
            '11','24','39','5'
        ])
        self.community_chest = CardDeck([
            '','','','',
            '','','','',
            '','','','',
            '','','0','10'
        ])
    
    def move(self,new_position):
        self.position = new_position
        self.hist[new_position] += 1

    def spread(self):
        s = float(sum(i for i in self.hist))
        return [(self.hist[i]/s,i) for i in xrange(40)]

    def turn(self):
        double = 0
        r1,r2 = -1,-1
        while r1 == r2:
            r1,r2 = (i.roll() for i in self.dice)
            if r1 == r2:
                double += 1
            new_position = (self.position+r1+r2)%40
            if double == 3 or new_position == 30:
                self.move(10)
                break
            elif new_position in (2,17,33):
                card = self.community_chest.draw()
                if len(card) > 0:
                    self.move(int(card))
                else:
                    self.move(new_position)
            elif new_position in (7,22,36):
                card = self.chance.draw()
                if len(card) > 0:
                    if card == 'rail':
                        if 15 > new_position > 5:
                            self.move(15)
                        elif 25 > new_position > 15:
                            self.move(25)
                        elif 35 > new_position > 25:
                            self.move(35)
                        else:
                            self.move(5)
                    elif card == 'util':
                        if 28 > new_position > 12:
                            self.move(28)
                        else:
                            self.move(12)
                    else:
                        card = int(card)
                        if card < 0:
                            self.move(new_position-3)
                        else:
                            self.move(int(card))
                else:
                    self.move(new_position)
            else:
                self.move(new_position)

h = [0]*40
games = 1#10**2
turns = 10**6
for game in xrange(games):
    b = Board()
    for turn in xrange(turns):
        b.turn()
    for i in xrange(40):
        h[i] += b.hist[i]

def pad(n):
    s = str(n)
    if len(s) < 2:
        return "0"+s
    return s

p = float(sum(h))
print ''.join(pad(j[1]) for j in sorted([(h[i]/p,i) for i in xrange(40)])[::-1][:3])

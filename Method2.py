import random


# Method 2
# In this method we also get the same thing but the difference is that we know what card we got and its rank and value
cards = []
suits = ["Spades","clubs","hearts","diamonds"]
ranks = [{"rank":"A","value":11,
         "rank":"1","value":1,
         "rank":"2","value":2,
         "rank":"3","value":3,
         "rank":"4","value":4,
         "rank":"5","value":5,
         "rank":"6","value":6,
         "rank":"7","value":7,
         "rank":"8","value":8,
         "rank":"9","value":9,
         "rank":"J","value":10,
         "rank":"Q","value":10,
         "rank":"K","value":10,}]


for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])

random.shuffle(cards)


def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_dealt = []
    for x in range(number):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt

shuffle()
card = deal(1)[0]

print(card)
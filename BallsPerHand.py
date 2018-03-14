import random
y = []
card = []
hand = []

def col_maker(col_num,spots):
    global card
    nums = list(range(15*(col_num-1)+1,15*(col_num-1)+16))
    col = []
    while(len(col) <= spots):
        q = len(col)
        while(len(col) == q):
            r = random.choice(nums)
            if(r not in card):
                col.append(r)
            else:
                print('fail',r,col)
    for t in col:
        card.append(t)

def card_maker():
    global hand, card
    col_maker(1,5)
    col_maker(2,5)
    col_maker(3,4)
    col_maker(4,5)
    col_maker(5,5)
    for t in card:
        hand.append(t)
    hand = list(set(hand))
    card = []

def main():
    card_maker()
    card_maker()
    card_maker()
    card_maker()
    return len(hand)

for t in range(1000000):
    j = main()
    #print(j)
    y.append(j)
    hand = []

for e in range(24,76):
    print(e,y.count(e))



print('done')

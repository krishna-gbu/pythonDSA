
cards=[12,10,9,8,7,6,5,4,3,2,1]
def locate_card(cards,no):
    if len(cards) < 0 : return -1
    for index,card in enumerate(cards):
        if card == no:
            print('index of card and no on card',index, card)
            return index+1
    return -1



print(locate_card(cards,5))
from card import Card
import random
class Deck:
    '''
    Class đại diện cho bộ bài, bao gồm 36 lá
    '''
    v = [2, 3, 4, 5, 6, 7, 8, 9,1]
    s = ['♠', '♣', '♦', '♥']
    
    def build(self):
        '''Tạo bộ bài'''
        self.deck = []
        for i in Deck.v:
            for j in Deck.s:
                self.deck.append(Card(i,j))
        for i in self.deck:
            print(i)
        

    def shuffle_card(self):
        '''Trộn bộ bài'''
        random.shuffle(self.deck)
        for i in self.deck:
            print(i)

    def deal_card(self,index_card):
        '''Rút một lá bài từ bộ bài'''
        return self.deck[index_card]
        

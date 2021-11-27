class Card:
    '''
    Class đại diện cho mỗi lá bài

    Mỗi lá bài bao gồm rank ('A', 1, 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    '''
    

    def __init__(self,v,s):
        self.v=v
        self.s = s

    def __str__(self):
        '''Hiển thị lá bài'''
        return (str(self.v) + self.s)

    def __gt__(self, other):
        '''So sánh 2 lá bài'''
        if Card.r.index(self.r)== Card.r.index(other.r):
            return Card.s.index(self.s)> Card.s.index(other.s)
        else:
            return Card.r.index(self.r)> Card.r.index(other.r)

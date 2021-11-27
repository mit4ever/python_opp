class Player:
    '''
    Class đại diện cho mỗi người chơi

    Người chơi chỉ cần lưu tên, và các lá bài người chơi có
    '''

    def __init__(self,name):  # dễ
        self.name = name
        self.card = []

    @property
    def point(self):  # trung bình
        '''Tính điểm cho bộ bài'''
        total = 0
        for i in self.card:
            total += i.v
        return (total%10)

    @property
    def biggest_card(self):
        '''
        Tìm lá bài lớn nhất
        Trong trường hợp điểm bằng nhau, sẽ so sánh lá bài lớn nhất để tìm ra người chiến thắng
        '''
        max = self.card[0]
        for card in self.card:
            if card > max:
                max = card
        return max
    def add_card(self,card):
        '''Thêm một lá bài vào bộ (rút từ bộ bài)'''
        self.card.append(card)s

       
    def remove_card(self):
        '''Reset bộ bài khi chơi game mới'''
        self.card=[]
    def flip_card(self):
        '''Lật bài, hiển thị các lá bài'''
            
        for i in self.card:
            print(i)

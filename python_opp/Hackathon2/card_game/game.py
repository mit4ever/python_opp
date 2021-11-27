from player import Player
from deck import Deck
class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''

    def __init__(self):
        self.number = []
        self.deck = Deck()
        self.deck.build()
    def setup(self):
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        print("Well come........., nhập số người chơi")
        number_player = int(input())
        name=[]
        for i in range(number_player):
            name_player = input("Nhập tên người chơi thứ " +str(i+1))
            self.number.append(Player(name_player))

    def guide(self):
        '''Hiển thị menu chức năng/hướng dẫn chơi'''
        print("1. Danh sách người chơi")
        print("2. Thêm người chơi")
        print("3. Loại người chơi")
        print("4. Chia bài")
        print("5. Lật bài")
        print("6. Xem lại game vừa chơi")
        print("7. Xem lịch sử chơi hôm nay")
        print("8. Công an tới, tốc biến :)")

    def list_players(self):
        '''Hiển thị danh sách người chơi'''
        print("Danh sách người chơi là: ")
        for i in self.number:
            print(i)

    def add_player(self):
        '''Thêm một người chơi mới'''
        name = input("Nhập tên người chơi muốn thêm: ")
        self.number.append(Player(name))

    def remove_player(self):
        '''
        Loại một người chơi
        Mỗi người chơi có một ID (có thể lấy theo index trong list)
        '''
        number_player = int(input("Bạn muốn xóa người chơi thứ mấy? "))
        self.number.pop(number_player)

    def deal_card(self):
        '''Chia bài cho người chơi'''
        n = len(self.number)
        for player in self.number:
            player.add_card(self.deck.deal_card(self.number.index(player)))
            player.add_card(self.deck.deal_card(self.number.index(player + n)))
            player.add_card(self.deck.deal_card(self.number.index(player + 2*n)))
    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        for player in self.number:
            player.point()
    
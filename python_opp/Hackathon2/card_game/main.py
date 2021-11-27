from game import Game

def main():  # khó
    '''Khởi tạo trò chơi, hiển thị menu và thực thi các chức năng tương ứng'''
    user = Game()
    user.setup()
    user.guide()
    option = int(input("Chọn option:"))
    while option != 8:
        if option == 1:
            user.list_players() 
        if option == 2:
            user.add_player()
        if option == 3:
            user.remove_player()
        if option == 4:
            user.deal_card()
        user.guide()
        option = int(input("Chọn option:"))

if __name__ == '__main__':
    main()

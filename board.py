class Board:
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 2],
                      [0, 0, 0, 0, 0, 0, 3], [0, 0, 0, 0, 0, 0, 4]
            , [0, 0, 0, 0, 0, 0, 5], [0, 0, 0, 0, 0, 0, 6]]

    def print_board(self):

        print("1|2|3|4|5|6|7")
        print("+-+-+-+-+-+-+")
        temp = ""
        aux = 1
        for row in self.board:
            for value in row:
                if aux % 7 != 0:
                    temp += " | " + str(value)
                if aux % 7 == 0:
                    temp += f" | {str(value)} | {aux // 7} \n"
                aux += 1
        print(temp)

    def update_board(self, column, player):

        if player == 1:
            player_mark = "X"
        else:
            player_mark = "U"

        column -= 1
        aux_row = 6

        if 0 <= column < 7:
            for _ in self.board:
                aux_row -= 1
                for i in range(6, 0, -1):
                    if self.board[aux_row][column] == 0:
                        self.board[aux_row].pop(column)
                        self.board[aux_row].insert(column, player_mark)
                        return


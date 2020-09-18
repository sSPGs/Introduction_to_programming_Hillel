class Desk:

    def __init__(self):
        self.desk = self.my_empty_desk()
        self.desk_print = self.print_my_desk()

    def __repr__(self):
        count_of_pawns = self.desk_print.count("Pawn")
        count_of_rook = self.desk_print.count("Rook")
        count_of_knight = self.desk_print.count("Knight")
        count_of_bishop = self.desk_print.count("Bishop")
        count_of_queen = self.desk_print.count("Queen")
        count_of_king = self.desk_print.count("King")
        return f"Количество фигур на доске:\n" \
               f"Пешка: {count_of_pawns}\n" \
               f"Конь: {count_of_knight}\n" \
               f"Слон: {count_of_bishop}\n" \
               f"Ладья: {count_of_rook}\n" \
               f"Ферзь: {count_of_queen}\n" \
               f"Король: {count_of_king}\n"

    def my_empty_desk(self):
        desk = {"A" : {"1": "Пусто","2": "Пусто","3": "Пусто","4": "Пусто","5": "Пусто","6": "Пусто","7": "Пусто","8": "Пусто"},
        "B" : {"1": "Пусто","2": "Пусто","3": "Пусто","4": "Пусто","5": "Пусто","6": "Пусто","7": "Пусто","8": "Пусто"},
        "C" : {"1": "Пусто","2": "Пусто","3": "Пусто","4": "Пусто","5": "Пусто","6": "Пусто","7": "Пусто","8": "Пусто"},
        "D" : {"1": "Пусто","2": "Пусто","3": "Пусто","4": "Пусто","5": "Пусто","6": "Пусто","7": "Пусто","8": "Пусто"},
        "E" : {"1": "Пусто","2": "Пусто","3": "Пусто","4": "Пусто","5": "Пусто","6": "Пусто","7": "Пусто","8": "Пусто"},
        "F" : {"1": "Пусто","2": "Пусто","3": "Пусто","4": "Пусто","5": "Пусто","6": "Пусто","7": "Пусто","8": "Пусто"},
        "G" : {"1": "Пусто","2": "Пусто","3": "Пусто","4": "Пусто","5": "Пусто","6": "Пусто","7": "Пусто","8": "Пусто"},
        "H" : {"1": "Пусто","2": "Пусто","3": "Пусто","4": "Пусто","5": "Пусто","6": "Пусто","7": "Пусто","8": "Пусто"}}
        return desk

    def print_my_desk(self):
        my_desk_print = """
        | A8 | B8 | C8 | D8 | E8 | F8 | G8 | H8 |
        | A7 | B7 | C7 | D7 | E7 | F7 | G7 | H7 |
        | A6 | B6 | C6 | D6 | E6 | F6 | G6 | H6 |
        | A5 | B5 | C5 | D5 | E5 | F5 | G5 | H5 |
        | A4 | B4 | C4 | D4 | E4 | F4 | G4 | H4 |
        | A3 | B3 | C3 | D3 | E3 | F3 | G3 | H3 |
        | A2 | B2 | C2 | D2 | E2 | F2 | G2 | H2 |
        | A1 | B1 | C1 | D1 | E1 | F1 | G1 | H1 |
                            """
        return my_desk_print

    def get_piece_on(self, place):
        piece_type = self.desk[place[0]][place[-1]]
        return piece_type

    def remove_piece_from(self, place):
        piece_type = self.desk[place[0]][place[-1]]
        desk = self.desk
        desk[place[0]][place[-1]] = place
        my_desk = self.desk_print
        self.desk_print = my_desk.replace(piece_type, place, 1)

    def add_piece_on(self, place, type_piece):
        desk = self.desk
        desk[place[0]][place[-1]] = place + "/" + type_piece
        my_desk = self.desk_print
        self.desk_print = my_desk.replace(place, place + "/" + type_piece)

desk = Desk()
desk.add_piece_on("A2", "Pawn")
desk.add_piece_on("B2", "Pawn")
desk.add_piece_on("C2", "Pawn")
desk.add_piece_on("D2", "Pawn")
desk.add_piece_on("E2", "Pawn")
desk.add_piece_on("F2", "Pawn")
desk.add_piece_on("G2", "Pawn")
desk.add_piece_on("H2", "Pawn")
desk.add_piece_on("A1", "Bishop")
desk.add_piece_on("H1", "Bishop")
desk.add_piece_on("B1", "Knight")
desk.add_piece_on("G1", "Knight")
desk.add_piece_on("C1", "Rook")
desk.add_piece_on("F1", "Rook")
desk.add_piece_on("D1", "King")
desk.add_piece_on("E1", "Queen")
print(desk.desk_print)
print(desk)
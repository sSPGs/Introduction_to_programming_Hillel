class Piece:
    def __init__(self, color, place):
        self.color = color # Цвет фигуры
        self.place = place # Координата фигуры
        self.moves = [] # Возможные ходы фигуры
        self.takes = [] # Возможные атаки фигуры
        self.target = "" # Цель атаки/хода

    def __repr__(self):
        return f"----------------\n" \
               f"color: {self.color}\n" \
               f"place: {self.place}\n" \
               f"target: {self.target}\n" \
               f"moves: {self.moves}\n" \
               f"takes: {self.takes}\n" \
               f"----------------"

    def get_moves(self):
        raise Exception("must override in child class")

    def get_takes(self):
        raise Exception("must override in child class")

    def new_target(self):
        raise Exception("must override in child class")

    def _get_cell_up(self, place: str, piece_move = 1):
        all_place_up = []
        place_number = int(place[-1])
        pawn_move = place_number + piece_move
        while place_number != pawn_move:
            new_number = place_number + 1 if place_number < 8 else place_number
            new_place = place.replace(str(place_number), str(new_number))
            all_place_up.append(new_place)
            place = new_place
            place_number += 1
        return all_place_up

    def _get_cell_down(self, place: str, piece_move = 1):
        all_place_down = []
        place_number = int(place[-1])
        pawn_move = place_number - piece_move
        while place_number != pawn_move:
            new_number = place_number - 1 if place_number > 1 else place_number
            new_place = place.replace(str(place_number), str(new_number))
            all_place_down.append(new_place)
            place = new_place
            place_number -= 1
        return all_place_down

    def _get_cell_left(self, place: str):
        all_place_left = []
        place_symbol = place[0]
        while place_symbol != "A":
            new_symbol = chr(ord(place_symbol) - 1) if place_symbol != "A" else place_symbol
            new_place = place.replace(place_symbol, new_symbol)
            all_place_left.append(new_place)
            place = new_place
            place_symbol = new_symbol
        return all_place_left # Новая буква

    def _get_cell_right(self, place: str):
        all_place_right = []
        place_symbol = place[0]
        while place_symbol != "H":
            new_symbol = chr(ord(place_symbol) + 1) if place_symbol != "H" else place_symbol
            new_place = place.replace(place_symbol, new_symbol)
            all_place_right.append(new_place)
            place = new_place
            place_symbol = new_symbol
        return all_place_right

    def _get_cell_diagonal_left_up(self, place: str, piece_move = 1):
        count = 1
        all_diagonal_left_up = []
        cell_up = self._get_cell_up(place, piece_move)
        for place_symbol in cell_up:
            new_symbol = place_symbol.replace(place_symbol[0], chr(ord(place_symbol[0]) - count))
            if "@" not in new_symbol:
                all_diagonal_left_up.append(new_symbol)
                count += 1
        return all_diagonal_left_up

    def _get_cell_diagonal_right_up(self, place: str, piece_move = 1):
        count = 1
        all_diagonal_right_up = []
        cell_up = self._get_cell_up(place, piece_move)
        for place_symbol in cell_up:
            new_symbol = place_symbol.replace(place_symbol[0], chr(ord(place_symbol[0]) + count))
            if "I" not in new_symbol:
                all_diagonal_right_up.append(new_symbol)
                count += 1
        return all_diagonal_right_up

    def _get_cell_diagonal_left_down(self, place: str, piece_move = 1):
        count = 1
        all_diagonal_left_down = []
        cell_down = self._get_cell_down(place, piece_move)
        for place_symbol in cell_down:
            new_symbol = place_symbol.replace(place_symbol[0], chr(ord(place_symbol[0]) - count))
            if "@" not in new_symbol:
                all_diagonal_left_down.append(new_symbol)
                count += 1
        return all_diagonal_left_down

    def _get_cell_diagonal_right_down(self, place: str, piece_move = 1) -> list:
        count = 1
        all_diagonal_right_down = []
        cell_down = self._get_cell_down(place, piece_move)
        for place_symbol in cell_down:
            new_symbol = place_symbol.replace(place_symbol[0], chr(ord(place_symbol[0]) + count))
            if "I" not in new_symbol:
                all_diagonal_right_down.append(new_symbol)
                count += 1
        return all_diagonal_right_down

class Pawn(Piece):
    def __init__(self, color, place):
        super().__init__(color, place)
        self.moves = self.get_moves()
        self.takes = self.get_takes()
        self.target = ""

    def get_moves(self):
        place_number = int(self.place[-1])
        if self.color == "white":
            new_place = self._get_cell_up(self.place) if place_number < 8 else self.place
        elif self.color == "black":
            new_place = self._get_cell_down(self.place) if place_number > 1 else self.place
        else:
            new_place = "Вы ввели неправильный цвет!"
        return [new_place]

    def get_takes(self, piece_move = 1) -> list:
        takes = []
        place_number = int(self.place[-1])
        if self.color == "white":
            if place_number != 8:
                takes.append(self._get_cell_diagonal_left_up(self.place))
                takes.append(self._get_cell_diagonal_right_up(self.place))
            else:
                takes.append("Атака влево невозможна!")
                takes.append("Атака вправо невозможна!")
        elif self.color == "black":
            if place_number != 1:
                takes.append(self._get_cell_diagonal_left_down(self.place))
                takes.append(self._get_cell_diagonal_right_down(self.place))
            else:
                takes.append("Атака влево невозможна!")
                takes.append("Атака вправо невозможна!")
        else:
            takes.append("Вы ввели неправильный цвет!")
        return takes

    def new_target(self):
        print("Введите цель: ")
        target = input()
        return target

    def move_to_target(self):
        self.place = self.new_target()
        self.moves = self.get_moves()
        self.takes = self.get_takes()
        self.target = ""


class Queen(Piece):

    def __init__(self, color, place):
        super().__init__(color, place)
        self.moves = self.get_moves()
        self.takes = self.get_takes()
        self.target = ""

    def get_moves(self):
        new_place = []
        place_number = int(self.place[-1])
        new_place.append(self._get_cell_up(self.place, (8 - place_number)))
        new_place.append(self._get_cell_down(self.place, (place_number - 1)))
        new_place.append(self._get_cell_left(self.place))
        new_place.append(self._get_cell_right(self.place))
        new_place.append(self._get_cell_diagonal_left_up(self.place ,(8 - place_number)))
        new_place.append(self._get_cell_diagonal_right_up(self.place ,(8 - place_number)))
        new_place.append(self._get_cell_diagonal_left_down(self.place ,(place_number - 1)))
        new_place.append(self._get_cell_diagonal_right_down(self.place ,(place_number - 1)))
        return new_place

    def get_takes(self):
        takes = self.get_moves()
        return takes

    def new_target(self):
        print("Введите цель: ")
        target = input()
        return target

    def move_to_target(self):
        self.place = self.new_target()
        self.moves = self.get_moves()
        self.takes = self.get_takes()
        self.target = ""



pawn = Pawn('white', 'D5')
print(pawn)
# pawn.move_to_target()
# print(pawn)


pawn = Queen('white', 'D5')
print(pawn)
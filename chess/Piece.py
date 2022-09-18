# def __init__(self, type):
#   self.type = type 

class Piece:
  def __init__(self, type = None):
    if type is not None: self.type = type
    print("hello", self.type)
 

class Pawn(Piece): type = 0 
class Bishop(Piece): type = 1 
class Knight(Piece): type = 2 
class Rook(Piece): type = 3 
class Queen(Piece): type = 4 
class King(Piece): type = 5 

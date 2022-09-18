import numpy as np
# import * as Piece from .Piece 
from chess.Piece import Piece

class Board:
  def __init__(self):
    print("test")
    self.squares = np.zeros((8, 8)) # create an 8 * 8 grid
    self.build()
  
  def render(self):
    for row in self.squares:
      for col in row:
        print("x")



        
  def build(self):
    self.place(0, 0, Piece.Pawn)
    
  def place(self, x, y, piece):
    self.squares[x][y] = piece

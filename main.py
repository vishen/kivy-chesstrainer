from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import SlideTransition, ScreenManager, Screen
from kivy import utils as kivy_utils
from kivy.lang import Builder

from ChessBoard import ChessBoard

SQUARES = ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "a6",
              "b6", "c6", "d6", "e6", "f6", "g6", "h6", "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "a4", "b4",
              "c4", "d4", "e4", "f4", "g4", "h4", "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "a2", "b2", "c2",
              "d2", "e2", "f2", "g2", "h2", "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]

img_piece_abv={"B":"WBishop", "R":"WRook", "N":"WKnight", "Q":"WQueen", "K":"WKing", "P": "WPawn",
"b":"BBishop", "r":"BRook", "n":"BKnight", "q":"BQueen", "k":"BKing", "p":"BPawn"}



# Builder.load_file('schess.kv')

class ChessApp(App):

    # chess_grid = ObjectProperty(None)

    def refresh_board(self, show_pieces=False, show_piece_coord=True, show_background_color=True):

        dark_color = (0.2, 0.3, 0.8, 0.5)
        light_color = (0.7, 0.7, 0.6, 1)
 
        # flatten lists into one list of 64 squares
        squares = [item for sublist in self.chessboard.getBoard() for item in sublist]
        print squares
        for i, p in enumerate(squares):
            light = i % 2 == (i / 8) % 2

            square = self.squares[i]

            if show_piece_coord:
                square.text = '%s' % SQUARES[i]

            if show_background_color:
                if light:
                    square.background_color = light_color

                else:
                    square.background_color = dark_color


    def build(self):
        self.chessboard = ChessBoard()
        self.squares = []

        # Had to manually load due to not being able to 
        # dynamically add buttons
        self.load_kv('chess.kv')
        
        root = self.root
        chess_grid = root.ids.chess_grid

        for square in SQUARES:
            bt = Button()

            chess_grid.add_widget(bt)
            self.squares.append(bt)

        self.refresh_board()

        return root


if __name__ == '__main__':
    ChessApp().run()
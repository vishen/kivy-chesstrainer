from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import SlideTransition, ScreenManager, Screen
from kivy import utils as kivy_utils

from ChessBoard import ChessBoard

SQUARES = ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "a6",
              "b6", "c6", "d6", "e6", "f6", "g6", "h6", "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "a4", "b4",
              "c4", "d4", "e4", "f4", "g4", "h4", "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "a2", "b2", "c2",
              "d2", "e2", "f2", "g2", "h2", "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]

img_piece_abv={"B":"WBishop", "R":"WRook", "N":"WKnight", "Q":"WQueen", "K":"WKing", "P": "WPawn",
"b":"BBishop", "r":"BRook", "n":"BKnight", "q":"BQueen", "k":"BKing", "p":"BPawn"}

class ChessApp(App):


    def refresh_board(self, show_pieces=False):
 
        # flatten lists into one list of 64 squares
        squares = [item for sublist in self.chessboard.getBoard() for item in sublist]
        print squares
        for i, p in enumerate(squares):
            sq = self.squares[i]
            sq.source = sq.background_down


    def build(self):
        self.from_move = None
        self.to_move = None
        self.chessboard = ChessBoard()
        self.squares = []
        self.use_engine = False
        self.last_touch_down_move = None
        self.last_touch_up_move = None

        parent = BoxLayout(size_hint=(1,1))
        # grid = GridLayout(cols=8, rows=8, padding=10, spacing=0, size=(575,575), size_hint=(0,0))
        grid = GridLayout(rows=8, padding=10, spacing=0)

        for i, name in enumerate(SQUARES):
            light = i % 2 == (i / 8) % 2

            background_color = (0.233, 0.166, 0.115, 0.8)
            background_normal = ''

            if not light:
                background_color = (1, 0, 0, 1)

            button_kwargs = {
                'text': '%s' % SQUARES[i],
                'background_color': background_color,
                'background_normal': background_normal,
            }
            bt = Button(**button_kwargs)
            


            grid.add_widget(bt)
            self.squares.append(bt)

        parent.add_widget(grid)

        self.refresh_board()

        # if self.is_desktop():
        #     self._keyboard = Window.request_keyboard(
        #         self._keyboard_closed, self)
        #     self._keyboard.bind(on_key_down=self._on_keyboard_down)

        #     self.start_engine_thread()

        sm = ScreenManager()
        board_screen = Screen(name='main')
        board_screen.add_widget(parent)
        sm.add_widget(board_screen)


        return sm


if __name__ == '__main__':
    ChessApp().run()
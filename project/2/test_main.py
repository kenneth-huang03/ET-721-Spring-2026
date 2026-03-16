import re
import unittest
from io import StringIO
from unittest.mock import patch

from main import Connect4

# THERE IS A LOT OF GOOGLING HERE BUT LIKE, I COULDN'T DO THIS WITH WHAT WE LEARNED
# THERE IS A LOT OF GOOGLING HERE BUT LIKE, I COULDN'T DO THIS WITH WHAT WE LEARNED
# THERE IS A LOT OF GOOGLING HERE BUT LIKE, I COULDN'T DO THIS WITH WHAT WE LEARNED
# THERE IS A LOT OF GOOGLING HERE BUT LIKE, I COULDN'T DO THIS WITH WHAT WE LEARNED

COLOUR_PATTERN = re.compile(r"\033\x5b9[0-9]m")

def terminal_to_string(game):
    with patch("sys.stdout", new_callable=StringIO) as stdout:
        game.print_board()
        return COLOUR_PATTERN.sub("", stdout.getvalue())


class TestPrintBoard(unittest.TestCase):

    def test_x_chip_rendered(self):
        game = Connect4()
        game.drop_chip(4) 
        game.switch_player()
        game.drop_chip(4)

        output = terminal_to_string(game)
        board_rows = [ln for ln in output.splitlines() if ln.startswith('|')]
        all_cells = ''.join(board_rows)
        self.assertIn('X', all_cells)


    def test_o_chip_rendered(self):
        """After switching to O and dropping a chip, print_board() must show 'O'."""
        game = Connect4()
        game.drop_chip(3)
        game.switch_player()
        game.drop_chip(5)
        
        output = terminal_to_string(game)
        board_rows = [ln for ln in output.splitlines() if ln.startswith('|')]
        all_cells = ''.join(board_rows)
        self.assertIn('O', all_cells)

    def test_x_chip_rendered(self):
        game = Connect4()
        game.drop_chip(4) 
        game.switch_player()
        game.drop_chip(4)

        output = terminal_to_string(game)
        board_rows = [ln for ln in output.splitlines() if ln.startswith('|')]
 
        # Row index 5 should contain 'X'
        self.assertIn('X', board_rows[5])
        # Row index 4 should contain 'O'
        self.assertIn('O', board_rows[4])
  

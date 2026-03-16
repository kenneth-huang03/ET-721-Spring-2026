import re
import pytest
from io import StringIO
from unittest.mock import patch

from main import Connect4


ANSI_ESCAPE = re.compile(r'\033\[[0-9]*m')

def run_game(inputs):
    # patch('builtins.input', side_effect=iter(inputs)) allows us to simulate a person typing in the console
    # patch('sys.stdout', new_callable=StringIO) allows us to capture output
    with patch('builtins.input', side_effect=iter(inputs)), patch('sys.stdout', new_callable=StringIO) as mock_out:
        Connect4().play_game()
    return ANSI_ESCAPE.sub('', mock_out.getvalue())


x_wins_inputs = ['1', '2', '1', '2', '1', '2', '1']
o_wins_inputs = ['1', '2', '1', '2', '1', '2', '3', '2']

# Idk how AI got this but it works
tie_inputs = ['1', '4', '7', '2', '5', '3', '6', '1', '4', '7', '2', '5', '3', '6', '1', '4', '7', '2', '5', '3', '6', '1', '4', '7', '2', '5', '3', '6', '1', '4', '7', '2', '5', '3', '6', '1', '4', '7', '2', '5', '3', '6']


class TestPlayGame:

    def test_x_wins_o_not_present(self):
        output = run_game(x_wins_inputs)
        assert "Player X wins!" in output
        assert "Player O wins!" not in output

    def test_o_wins_x_not_present(self):
        output = run_game(o_wins_inputs)
        assert "Player O wins!" in output
        assert "Player X wins!" not in output

    def test_tie_declared_when_board_full(self):
        output = run_game(tie_inputs)
        assert "It's a tie! No more moves left." in output
        assert "Player X wins!" not in output
        assert "Player O wins!" not in output

    def test_invalid_input_error(self):
        inputs = ['abc', 'e']
        output = run_game(inputs)
        assert "Invalid input. Please enter a number between 1 and 7." in output

    def test_out_of_range_column_shows_error(self):
        inputs = ['0', 'e']
        output = run_game(inputs)
        assert "Invalid move! Column is full or out of range. Try again." in output

    def test_full_column_shows_error(self):
        fill_col7 = ['7', '7', '7', '7', '7', '7', '7', 'e']         
        output = run_game(fill_col7)
        assert "Invalid move! Column is full or out of range. Try again." in output

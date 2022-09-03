from project import *
import pytest

def test_global():
    assert board == [
        '-','-','-',
        '-','-','-',
        '-','-','-'
    ]
    assert PLAYER == "X"
    assert COMPUTER == "O"
    assert turn == ""

def test_makeComputerMove():
    # keeping player X and computer O
    assert makeComputerMove([
        'X','X','-',
        '-','O','-',
        'O','-','-'
    ]) == 2

    assert makeComputerMove([
        '-','-','-',
        'X','X','-',
        'O','O','-'
    ]) == 8

    assert makeComputerMove([
        'O','O','X',
        '-','X','-',
        '-','-','-'
    ]) == 6

    assert makeComputerMove([
        'X','O','-',
        'X','-','O',
        '-','-','-'
    ]) == 6

    assert makeComputerMove([
        'X','O','O',
        'O','X','X',
        'X','O','O'
    ]) == 0

def test_minimax():
    assert minimax([
        'X','O','-',
        'X','O','-',
        '-','O','-'
    ], 0, False) == 1

    assert minimax([
        'X','X','O',
        '-','O','X',
        '-','O','O'
    ], 0, False) == 0


    assert minimax([
        'X','X','O',
        'O','-','X',
        '-','O','O'
    ], 0, True) == 1

    assert minimax([
        'X','X','O',
        '-','-','X',
        'O','O','O'
    ], 0, False) == 1


def test_validate_win():
    assert validate_win([
        '-','-','-',
        '-','-','-',
        '-','-','-'
    ]) == None

    assert validate_win([
        'X','X','X',
        '-','O','O',
        '-','-','-'
    ]) == "X"

    assert validate_win([
        'O','X','X',
        '-','O','-',
        '-','-','X'
    ]) == None

    assert validate_win([
        'O','-','X',
        '-','O','X',
        '-','X','O'
    ]) == "O"

    assert validate_win([
        'X','-','O',
        'X','O','-',
        'X','-','-'
    ]) == "X"

    assert validate_win([
        '-','O','-',
        'X','X','X',
        '-','O','-'
    ]) == "X"

def test_row_checker():
    assert row_checker([
        'X','X','X',
        '-','-','O',
        'O','-','-'
    ]) == "X"

    assert row_checker([
        'X','-','O',
        'O','X','-',
        '-','-','X'
    ]) == None

def test_column_checker():
    assert column_checker([
        'X','O','-',
        'X','-','-',
        'X','O','-'
    ]) == "X"

    assert column_checker([
        'O','O','O',
        '-','X','-',
        '-','-','X'
    ]) == None

def test_diagonal_checker():
    assert diagonal_checker([
        'X','-','-',
        '-','X','O',
        '-','O','X'
    ]) == "X"

    assert diagonal_checker([
        'X','O','X',
        'O','X','O',
        'O','X','O'
    ]) == None

def test_validate_tie():
    assert validate_tie([
        'X','O','X',
        'O','X','O',
        'O','X','O'
    ]) == "tie"

    assert validate_tie([
        'X','O','O',
        '-','X','-',
        '-','-','X'
    ]) == None

    assert validate_tie([
        'X','-','O',
        'X','-','O',
        '-','-','-'
    ]) == None

    assert validate_tie([
        'X','O','X',
        'X','O','O',
        'O','X','X'
    ]) == "tie"
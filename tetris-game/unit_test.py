import unittest

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter, QColor
import tetris_game
import tetris_model

class TestGame(unittest.TestCase):

    def test_init(self):
        app = QApplication([])
        tetris = tetris_game.Tetris()
        self.assertEqual(True, tetris.isStarted)
        self.assertEqual('Tetris', tetris.windowTitle())

    def test_pause(self):
        app = QApplication([])
        tetris = tetris_game.Tetris()
        tetris.pause()
        self.assertEqual(True, tetris.isPaused)

    def test_draw_shape(self):
        painter = QPainter()
        shape = tetris_game.drawSquare(painter, 1, 2, 0 , 10)
        self.assertEqual(None, shape)

class TestModel(unittest.TestCase):

    def test_init(self):
        shape = tetris_model.Shape()
        self.assertEqual(0, shape.shape)

    def test_getRotatedOffsets(self):
        shape = tetris_model.Shape()
        res = shape.getRotatedOffsets(0)
        self.assertNotEqual(None, res)

class TestBoardData(unittest.TestCase):

    def test_init(self):
        board_data = tetris_model.BoardData()
        self.assertEqual(0, board_data.currentDirection)

    def test_createNewPiece(self):
        board_data = tetris_model.BoardData()
        res = board_data.createNewPiece()
        self.assertEqual(True, res)
        
    def test_dropDown(self):
        board_data = tetris_model.BoardData()
        res = board_data.dropDown()
        self.assertEqual(0, res)

    def test_removeFullLines(self):
        board_data = tetris_model.BoardData()
        res = board_data.removeFullLines()
        self.assertEqual(0, res)
    
    def test_clear(self):
        board_data = tetris_model.BoardData()
        board_data.clear()
        self.assertEqual(0, board_data.currentDirection)
    

if __name__ == '__main__':
    unittest.main()
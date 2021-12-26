import sys, random
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPainter, QColor, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from tetris_game import Tetris

class startGame(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Start Game'
        self.initUI()

    def initUI(self): 
        self.setWindowTitle(self.title)

        self.textbox = QLineEdit(self)
        self.textbox.move(100, 50)
        self.textbox.resize(75,20)
        self.textbox.setPlaceholderText('Your name')

        button1 = QPushButton('Start game', self)
        button1.setToolTip('Press this button if you want to play alone')
        button1.move(100,80)
        button1.clicked.connect(self.play_alone)

        button2 = QPushButton('Start AI Game', self)
        button2.setToolTip('Press this button if you want AI to play instead of you')
        button2.move(100, 100)
        button2.clicked.connect(self.play_ai)

        self.show()

    @pyqtSlot()
    def play_alone(self):
        playerName = self.textbox.text()
        self.game = Tetris(playerName, False)
        self.game.show()
        self.hide()

    @pyqtSlot()
    def play_ai(self):
        playerName = self.textbox.text()
        self.game = Tetris(playerName, True)
        self.game.show()
        self.hide()

if __name__ == '__main__':
    # random.seed(32)
    app = QApplication([])
    startWindow = startGame()
    sys.exit(app.exec_()) 
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

        button = QPushButton('Start game', self)
        button.setToolTip('Press this button if you want to play alone')
        button.move(100,80)
        button.clicked.connect(self.play_alone)
        
        self.show()

    @pyqtSlot()
    def play_alone(self):
        playerName = self.textbox.text()
        self.game = Tetris(playerName)
        self.game.show()
        self.hide()
    
if __name__ == '__main__':
    # random.seed(32)
    app = QApplication([])
    startWindow = startGame()
    sys.exit(app.exec_())
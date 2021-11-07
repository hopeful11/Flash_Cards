from PyQt5 import QtWidgets, uic
import sys
from game import Game

class Menu(QtWidgets.QDialog):

    def __init__(self,name):
        self.name=name
        super(Menu, self).__init__()
        uic.loadUi('ui/menu.ui', self)
        self.label_username.setText(self.name)
        self.pushButton.clicked.connect(self.play)
        self.show()

    def play(self):
        self.cams = Game(self.name)
        self.cams.show()
        self.close()


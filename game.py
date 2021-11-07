from PyQt5 import QtWidgets, uic
import sys
import menu
import time
class Game(QtWidgets.QDialog):

    total_list = ['ik', 'ben', 'woon', 'werk', 'auto','mogen', 'over', 'tegen', 'komen', 'boom']
    point = 0
    notremember = 0
    word=""

    def __init__(self,name):
        self.name=name
        super(Game, self).__init__()
        uic.loadUi('ui/game_screen.ui', self)
        self.quitButton.clicked.connect(self.back)
        self.timer()
        self.show()

    def back(self):
        self.cams = menu.Menu(self.name)
        self.cams.show()
        self.close()

    def timer(self):
        word_list = self.total_list[:10]
        while self.point != 10:
            word_list1 = []
            print(f'first {word_list}')
            for i in word_list:
                word = i
                print(word)
                print('Timer 3 seconds！')
                time.sleep(1)                                      
                print('3')                                          
                time.sleep(1)                                        
                print('2')                                          
                time.sleep(1)                                        
                print('1')                                    
                choise = input('time out! true ortt false : ')
            print(f'list {word_list}')
        word_list = word_list1


    """#def true(self):
        self.point += 1
        print(f'your point {self.point}')
    def false(self):
        if not for i in self.word_list1:
            self.word_list1.append(self.word)
            self.notremember += 1
            print(f'notremember {self.notremember}')
        else:
            break"""

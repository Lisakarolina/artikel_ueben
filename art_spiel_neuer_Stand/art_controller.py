from PyQt5 import QtWidgets, uic, QtGui
import sys
import random
import logic


class Ui(QtWidgets.QDialog): #QMainWindow
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('oberfläch.ui', self) # Load the .ui file
    
        self.title = 'Artikel üben'
        self.setWindowTitle(self.title)

        self.q = logic.Question()   # create new question: a word is randomly chosen
        
        self.feld = self.findChild(QtWidgets.QLabel, 'wortfeld')
        self.feld.setText(self.q.subst)

        self.derk = self.findChild(QtWidgets.QPushButton, 'der_knopf')
        self.diek = self.findChild(QtWidgets.QPushButton, 'die_knopf')
        self.dask = self.findChild(QtWidgets.QPushButton, 'das_knopf')
        self.tfeld = self.findChild(QtWidgets.QLabel, 'tipfeld')
        self.bfeld = self.findChild(QtWidgets.QLabel, 'bewertfeld')
        self.bildfeld = self.findChild(QtWidgets.QLabel, 'bildfeld')

        self.derk.clicked.connect(self.derPressed) 
        self.diek.clicked.connect(self.diePressed)
        self.dask.clicked.connect(self.dasPressed)

        self.weiterk = self.findChild(QtWidgets.QPushButton, 'weiter_knopf')
        self.weiterk.clicked.connect(self.WeiterPressed)
        
        self.show()


    def WeiterPressed(self):
        """"if the weiter-button is pressed, make sure a question is created"""

        self.q = logic.Question()
        
        self.tfeld.setText('')
        self.bfeld.setText('')
        self.bfeld.setPixmap(QtGui.QPixmap(''))
        self.feld.setText(self.q.subst)
        


    def derPressed(self):
        """so the der-button has been pressed. differentiate reactions in relation to correct answer"""
        
        if self.q.art == 'der':
            self.bfeld.setPixmap(QtGui.QPixmap('neusmiley.jpg'))
        else:
            self.bfeld.setText('Leider nicht richtig. Versuch es noch einmal!')

        if self.q.art == 'das':
            self.tfeld.setText(self.q.der_das())
            
        if self.q.art == 'die':
            self.tfeld.setText(self.q.der_die())
    
        
            

    def diePressed(self):
        if self.q.art == 'die':
            self.bfeld.setPixmap(QtGui.QPixmap('neusmiley.jpg'))   
        else:
            self.bfeld.setText('Leider nicht richtig. Versuch es noch einmal!')
            
        if self.q.art == 'der':
            self.tfeld.setText(self.q.die_der())

        if self.q.art == 'das':
            self.tfeld.setText(self.q.die_das())

            


    def dasPressed(self):
        if self.q.art == 'das':
            self.bfeld.setPixmap(QtGui.QPixmap('neusmiley.jpg'))
        else:
            self.bfeld.setText('Leider nicht richtig. Versuch es noch einmal!')

        if self.q.art == 'der':
            self.tfeld.setText(self.q.das_der()) 

        if self.q.art == 'die':
            self.tfeld.setText(self.q.das_die())
            
    



app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
sys.exit(app.exec_())

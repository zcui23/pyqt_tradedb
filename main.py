import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from formswindow import FormWidget

'''
import sqlalchemy
'''


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.form_widget = FormWidget()
        self.setCentralWidget(self.form_widget)


        quitAction = QAction('&Quit', self)
        quitAction.setShortcut('Ctrl+Q')
        quitAction.setStatusTip('Leave The App')

        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(quitAction)

        quitAction.triggered.connect(self.quit_app)

    def quit_app(self):

        sys.exit()


'''
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine('mssql+pyodbc://DESKTOP-G57CRT2/fxtrading')
con = engine.connect()
rs = con.execute('select * from FundamentalData')
'''




def run():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

run()
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *





class FormWidget(QWidget):
    def __init__(self):
        super(FormWidget, self).__init__()
        self.layout = QVBoxLayout(self)
        self.setWindowTitle('PyQt test App')
        self.setGeometry(150, 150, 500, 300)

### execution time

        self.datelabel = QLabel('Please enter time:')
        self.dateline = QDateTimeEdit()
        self.dateline.setDateTime(QDateTime.currentDateTime())

### instrument name

        self.instrumentlabel = QLabel('Please enter instrument Symbol:')
        self.instrumentline = QLineEdit()

### position
        
        self.longbtn = QRadioButton('long')
        self.longbtn.toggled.connect(self.long_clicked)

        self.shortbtn = QRadioButton('short')
        self.shortbtn.toggled.connect(self.short_clicked)

### execution price

        self.pricelabel = QLabel('Please enter execution price:')

        self.priceline = QLineEdit()

        self.priceline.setText('0')

        self.execprice = self.priceline.text()
        try:
            self.execprice = float(self.execprice)
        except Exception:
            QMessageBox.about(self, 'Error', 'please enter a numeric value')

### execution quantity
        
        self.quantitylabel = QLabel('Please enter quantity:')


        self.quantityline = QLineEdit()
        self.quantityline.setText('0')
        self.quantity = self.quantityline.text()
        try:
            self.quantity = int(self.quantity)
        except Exception:
            QMessageBox.about(self, 'Error', 'please enter an integer')


### Submit Button

        self.btn = QPushButton('Click', self)

        self.btn.resize(self.btn.sizeHint())
        self.btn.move(220, 300)
        self.btn.setObjectName("submit_data")


        self.connect(self.btn, SIGNAL("clicked()"), self.submit_btn)


        self.layout.addWidget(self.datelabel)
        self.layout.addWidget(self.dateline)
        self.layout.addWidget(self.instrumentlabel)
        self.layout.addWidget(self.instrumentline)
        self.layout.addWidget(self.longbtn)
        self.layout.addWidget(self.shortbtn)
        self.layout.addWidget(self.pricelabel)
        self.layout.addWidget(self.priceline)
        self.layout.addWidget(self.quantitylabel)
        self.layout.addWidget(self.quantityline)
        self.layout.addWidget(self.btn)

        self.setLayout(self.layout)

    def long_clicked(self):
        return 'long'
    def short_clicked(self):
        return 'short'    


    def submit_btn(self):
        exectime = self.dateline.dateTime()
        instrument = self.instrumentline.text()

        if self.longbtn.isChecked():
            position = self.long_clicked()
        elif self.shortbtn.isChecked():
            position = self.short_clicked()
        

        execprice = float(self.priceline.text())
        quantity = int(self.quantityline.text())

        print(exectime, instrument, position, execprice, quantity)

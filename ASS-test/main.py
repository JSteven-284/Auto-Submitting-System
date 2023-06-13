import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from Ui_Auto_submitting_system import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow): #这里也要记得改
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
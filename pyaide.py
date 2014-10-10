
import sys
import os
from PyQt4 import QtGui
import ino.runner as ino

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):

        exitAction = QtGui.QAction('&New', self)
        exitAction.setStatusTip('Create')
        exitAction.triggered.connect(self.newProj)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Project')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Python Arduino IDE')
        self.show()

    def newProj(self):

        text, ok = QtGui.QInputDialog.getText(self, 'New Project', 'Name:')

        if ok:
            file = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
            file = os.path.join(file, str(text))
            try:
                os.mkdir(file)
                os.chdir(file)
                sys.argv = ['', 'init', '-t', 'blink']
                ino.main()
            except Exception, e:
                raise

def main():

    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
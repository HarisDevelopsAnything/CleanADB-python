import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QScrollArea
from PyQt5.QtCore import Qt
import subprocess

class CheckList(QWidget):
    def __init__(self):
        super().__init__()

        # Create a scroll area widget
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setGeometry(50, 50, 200, 200)
        self.neatlist= ""
        self.listApps()
        # Create the list widget
        self.list_widget = QListWidget(scroll)
        scroll.setWidget(self.list_widget)

        # Add the items to the list widget
        
        for item in self.items:
            list_item = QListWidgetItem(item.replace("package:com.", "").replace("."," ").title(), self.list_widget)
            list_item.setFlags(list_item.flags() | Qt.ItemIsUserCheckable)
            list_item.setCheckState(Qt.Unchecked)

        self.show()
        self.listApps()
    def listApps(self):
        rawlist= str(subprocess.run('adb shell pm list package', shell=True, capture_output=True).stdout.decode())
        self.items= rawlist.split('\r\n')
        for item in self.items:
            self.neatlist+= item.replace("package:com.", "").replace("."," ")+","
        

        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CheckList()
    sys.exit(app.exec_())

import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("CSV 파일 뷰어")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.tableWidget = QTableWidget()
        self.layout.addWidget(self.tableWidget)

        self.loadButton = QPushButton("CSV 파일 불러오기")
        self.loadButton.clicked.connect(self.loadCSV)
        self.layout.addWidget(self.loadButton)

    def loadCSV(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)")

        if filePath:
            with open(filePath, "r", newline="") as file:
                self.tableWidget.clear()

                csvReader = csv.reader(file)
                csvList = list(csvReader)

                rowNum = len(csvList)
                colNum = len(csvList[0])

                self.tableWidget.setRowCount(rowNum)
                self.tableWidget.setColumnCount(colNum)

                header_list = csvList[0]
                self.tableWidget.setHorizontalHeaderLabels(header_list)

                for i in range(1, rowNum):
                    for k in range(colNum):
                        item = QTableWidgetItem(csvList[i][k])
                        if k == 6 and csvList[i][k].isnumeric() and int(csvList[i][k]) >= 167:
                            item.setBackground('yellow')
                        self.tableWidget.setItem(i - 1, k, item)

                self.tableWidget.resizeColumnsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
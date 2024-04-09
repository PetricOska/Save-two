import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
import requests
from bs4 import BeautifulSoup

class MovieRankingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("실시간 영화 순위")
        self.setGeometry(100, 100, 660, 966)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["순위", "제목", "예매율", "개봉일"])
        layout.addWidget(self.table)

        self.get_movie_ranking()

    def get_movie_ranking(self):
        url = 'https://www.moviechart.co.kr/rank/realtime/index/image'
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            movie_ranking = []
            for li in soup.select('li.movieBox-item'):
                rank = li.select_one('p.rank').text.strip()
                title = li.select_one('.movie-title h3 a').text.strip()  # 수정된 부분
                ticketing_rate = li.select_one('li.ticketing span').text.strip()
                release_date = li.select_one('li.movie-launch').text.strip().split(' : ')[1]

                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                self.table.setItem(row_position, 0, QTableWidgetItem(rank))
                self.table.setItem(row_position, 1, QTableWidgetItem(title))
                self.table.setItem(row_position, 2, QTableWidgetItem(ticketing_rate))
                self.table.setItem(row_position, 3, QTableWidgetItem(release_date))

        else:
            self.label = QLabel('Failed to fetch the webpage')
            self.label.setAlignment(Qt.AlignCenter)
            self.setCentralWidget(self.label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MovieRankingWindow()
    window.show()
    sys.exit(app.exec_())

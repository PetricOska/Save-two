import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
import requests
from bs4 import BeautifulSoup

class MovieRankingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("실시간 영화 순위")
        self.resize(660, 966)  # 윈도우 크기 조정

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)  # 수직 레이아웃 생성

        self.table = QTableWidget()  # 테이블 위젯 생성
        self.table.setColumnCount(4)  # 열 개수 설정
        self.table.setHorizontalHeaderLabels(["순위", "제목", "예매율", "개봉일"])  # 테이블 헤더 설정
        layout.addWidget(self.table)  # 테이블 위젯을 수직 레이아웃에 추가

        self.get_movie_ranking()  # 영화 순위 정보 가져오는 함수 호출

    def get_movie_ranking(self):
        # 웹페이지에서 영화 순위 정보를 가져오는 함수
        url = 'https://www.moviechart.co.kr/rank/realtime/index/image'  # 영화 순위 웹페이지 URL
        response = requests.get(url)  # 웹페이지에 GET 요청을 보냄

        if response.status_code == 200:  # 요청이 성공했을 경우
            soup = BeautifulSoup(response.text, 'html.parser')  # 응답 데이터를 BeautifulSoup으로 파싱
            for li in soup.select('li.movieBox-item'):  # 각 영화 정보를 포함하는 리스트 아이템에 대해 반복
                rank = li.select_one('p.rank').text.strip()  # 순위 정보 추출
                title = li.select_one('.movie-title h3 a').text.strip()  # 제목 정보 추출
                ticketing_rate = li.select_one('li.ticketing span').text.strip()  # 예매율 정보 추출
                release_date = li.select_one('li.movie-launch').text.strip().split(' : ')[1]  # 개봉일 정보 추출

                row_position = self.table.rowCount()  # 새로운 행의 위치 결정
                self.table.insertRow(row_position)  # 새로운 행 삽입
                # 각 열에 해당 정보를 QTableWidgetItem으로 추가
                self.table.setItem(row_position, 0, QTableWidgetItem(rank))
                self.table.setItem(row_position, 1, QTableWidgetItem(title))
                self.table.setItem(row_position, 2, QTableWidgetItem(ticketing_rate))
                self.table.setItem(row_position, 3, QTableWidgetItem(release_date))

        else:  # 요청이 실패했을 경우
            self.label = QLabel('Failed to fetch the webpage')  # 실패 메시지 라벨 생성
            self.label.setAlignment(Qt.AlignCenter)  # 라벨을 중앙 정렬로 설정
            self.setCentralWidget(self.label)  # 실패 메시지 라벨을 중앙 위젯으로 설정

if __name__ == '__main__':
    app = QApplication(sys.argv)  # PyQt 애플리케이션 생성
    window = MovieRankingWindow()  # MovieRankingWindow 인스턴스 생성
    window.show()  # 윈도우 표시
    sys.exit(app.exec_())  # 애플리케이션 이벤트 루프 실행 및 종료

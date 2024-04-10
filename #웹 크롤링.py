import csv
import time
import datetime
import bs4import urllib.request

csvName = 'C:/CookAnalysis/CSV/sokcho_weather.csv'
with open(csvName, 'w', newline='') as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['연월일', '시분초', '온도', '습도', '강수량', '풍향'])

nateUrl = "https://search.daum.net/nate?w=tot&DA=Z8T&q=%EA%B2%BD%EC%83%81%EB%82%A8%EB%8F%84%20%EC%A7%84%EC%A3%BC%EC%8B%9C%20%EB%82%A0%EC%94%A8&rtmaxcoll=Z8T"
while True :
    htmlObject = urllib.request.urlopen(nateUrl)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
    tag = bsObject.find('div', {'class': 'right_today'})
    temper = tag.find('p', ) #Ch09_웹 크롤링 44p
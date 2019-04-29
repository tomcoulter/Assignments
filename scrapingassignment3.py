import urllib2, csv
from bs4 import BeautifulSoup

csvfile = open('billtest.csv', 'a')
billtest_writer = csv.writer(csvfile)

url = 'https://www.senate.mo.gov/19info/BTS_Web/TrulyAgreed.aspx?SessionType=R'
html = urllib2.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table', {'id': 'Table2'})

for Table2 in tables:
    
    rows = Table2.find_all('tr')

    for row in rows:
        output_row = []

        cells = row.find_all('td')

        for cell in cells:
            output_row.append(cell.text)

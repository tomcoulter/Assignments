import urllib2, csv
#the above line imports the toolkit "urllib2" and writes it out as a csv module
from bs4 import BeautifulSoup
#this imports the "BeautifulSoup" toolkit from its library

outfile = open('jaildata.csv', 'w')
#anything exported will be saved as 'jaildata.csv' and I'm not really sure about the 'w'
writer = csv.writer(outfile)
#I think this allows us to decide the header tabs in HTML files

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
#this indicates the url source that will be scraped
html = urllib2.urlopen(url).read()
#this will use the toolkit established on the first line to open the url on Line 11

soup = BeautifulSoup(html, "html.parser")
#this makes soup equal to Beautiful Soup with the use of Python's HTML-parser

tbody = soup.find('tbody', {'class': 'stripe'})
#I think this instructs Beautiful Soup how to get the specific table we want

rows = tbody.find_all('tr')
#Rather than a specific table, this command would select all of them

for row in rows:
    #I'm not sure, but I think this will return a specific list of rows

    cells = row.find_all('td')
    #And this should give us the complete list of rows

    data = []
    #creates a list to enter the data
    for cell in cells:
    #establishes a cell for the data to go
        data.append(cell.text.encode('utf-8'))
        #this loop adds the utf-8 format to the list
        

    writer.writerow(data)
    #this sets the format for getting data into a list

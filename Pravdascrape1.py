from bs4 import BeautifulSoup
import requests

import csv

# source saves all the html elements of the webiste 
source = requests.get('https://canada.news-pravda.com/russia/2025/10/15/28473.html').text
#makes it format in nice format 
soup = BeautifulSoup(source ,'lxml')

# w is write 
csv_file = open('firstscrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Date published','Title','Article','Source'])


# first step find the tag that encompassess one article then we can loop it later 

# find the keyword of article
article = soup.find('article')

# time article published 
dates = article.find('div',class_='article__time').time.text
print(dates, end="\n")

title = article.h1.text
print(title, end="\n")


paragraph = article.find('div',class_='article__text').text
print(paragraph, end="\n")

source = article.find('div',class_='article__source').text
print(source)

# print(article.prettify())
csv_writer.writerow([dates,title,paragraph,source])

csv_file.close()
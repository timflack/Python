"""
scipt to show how to use beautfil soup to parse info from simple html file and example website
"""

import csv
from bs4 import BeautifulSoup
import requests

# create soup object with simple.html
# lxml is the parser, can use a number of them
with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())

# access title like attribute
match = soup.title.text
print(match)

# can use find to look for specific titles/divs etc
match = soup.find('div', class_='footer')
print(match)

# grab text of article headline
article = soup.find('div', class_='article')
headline = article.h2.a.text
print(headline)

# or the summary
summary = article.p.text
print(summary)

# can use findall to generate list of all matches
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.p.text
    print(summary)

# now move onto to a website
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

# grab headline, snippet and embedded video of first post on website
article = soup.find('article')
headline = article.h2.a.text
print(headline)
summary = article.find('div', class_='entry-content').p.text
print(summary)
vid_src = article.find('iframe', class_='youtube-player')['src']
print(vid_src)
vid_id = vid_src.split('/')[4]
print(vid_id)
vid_id = vid_id.split('?')[0]
print(vid_id)

# create youtube link with vid_id
yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)


# now loop over all articles in website and save to csv file
csv_file = open('scraped_results', 'w')
csv_writer = csv.writer(csv_file)
csv.writer.writerow(['headline', 'summary', 'link'])
for article in soup.find_all('article'):
    article = soup.find('article')
    headline = article.h2.a.text
    summary = article.find('div', class_='entry-content').p.text
    vid_src = article.find('iframe', class_='youtube-player')['src']
    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]
    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print('Headline = {}'.format, headline)
    print('Summary = {}'.format, summary)
    print('Link = {}'. format, yt_link)
    print()
    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()

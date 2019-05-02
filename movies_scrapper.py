from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv


movies_2018_link = 'https://www.imdb.com/list/ls058813655/'

movies_2017_link = ' '

movies_2016_link = ' '


u_client = uReq(movies_2018_link)
html_file = u_client.read()
u_client.close()

bsoup = soup(html_file, "html.parser")
lst = bsoup.findAll("h3", {"class": "lister-item-header"})


'''

for item in lst:
	print(item)
	break

ouput:

<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">1.</span>
<a href="/title/tt4154756/">Avengers: Infinity War</a>
<span class="lister-item-year text-muted unbold">(2018)</span>
</h3>

'''


cur_dir = 'C:/Users/amit/Desktop/reviews-ratings-scrapper'
out_file = open( cur_dir + '/datasets/movies.csv', 'w', newline='')
k = 1

#write index
words  = ['title', 'reviews_link']
writer = csv.writer(out_file)
writer.writerow(words)

for item in lst:

    title_tag = item.find("a", href = True)
    title = title_tag.text.strip()
    link = 'https://www.imdb.com' + title_tag['href'].split('?')[0] + 'reviews?ref_=tt_urv'
    if not title or not link:
        continue
    
    words  = [title, link]
    writer = csv.writer(out_file)
    writer.writerow(words)
    print("\n\nTitle: " + title + "\nLink: " + link)

'''
output:
Title: Avengers: Infinity War
Link: https://www.imdb.com/title/tt4154756/reviews?ref_=tt_urv
...
'''

out_file.close()




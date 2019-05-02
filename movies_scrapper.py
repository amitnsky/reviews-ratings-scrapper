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


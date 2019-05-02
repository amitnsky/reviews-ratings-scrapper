from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv
import time


cur_dir = 'C:/Users/amit/Desktop/reviews-ratings-scrapper'
out_file = open( cur_dir + '/datasets/reviews.csv', 'w', newline='', encoding="utf-8")
k = 1

head  = ['imdb_link', 'review_title', 'review', 'rating']
writer = csv.writer(out_file)
writer.writerow(head)

data_path = cur_dir + '/datasets/movies.csv'
movies_list = open(data_path).read().split('\n')



out_file.close()

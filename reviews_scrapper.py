from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv
import time


cur_dir = 'C:/Users/amit/Desktop/reviews-ratings-scrapper'
out_file = open( cur_dir + '/datasets/reviews.csv', 'w', newline='', encoding="utf-8")
k = 1

head  = ['imdb_link', 'review_title', 'review_text', 'rating']
writer = csv.writer(out_file)
writer.writerow(head)

data_path = cur_dir + '/datasets/movies.csv'
movies_list = open(data_path).read().split('\n')



# ignore first row, as it has header only
for movie in movies_list[1:len(movies_list)-1]:
    reviews_link = movie.split(',')[1]
    
    print(reviews_link + "\n")
    
    u_client = uReq(reviews_link)
    html_file = u_client.read()
    u_client.close()

    # verify program is working 
    #print(html_file)
    
    bsoup = soup(html_file, "html.parser")
    #bsoup = bsoup.encode("utf-8")
    lst = bsoup.findAll("div", {"class": "lister-item-content"})

    for item in lst:

        title_tag = item.find("a", {"class": "title"})
        rating_tag = item.find("span", {"class": "rating-other-user-rating"})
        review_tag = item.find('div', {'class': 'text show-more__control'})

        # if any field is not available ignore this review
        if not rating_tag or not review_tag or not title_tag:
            continue

        imdb_link = reviews_link
        review_title = title_tag.text.strip()
        review_text = review_tag.text.strip()
        rating = rating_tag.findChildren('span')[0].text.strip()

        '''
        # verify output
        print("\n\nReview page: " + imdb_link
            + "\nReview title: " + review_title
            + "\nReview text: " + review_text
            + "\nRating: " + rating)
        break

        output:
        Review page: https://www.imdb.com/title/tt4154756/reviews?ref_=tt_urv
        Review title: Unlike anything ever done in the history of cinema
        Review text: This movie is the beginning of t....
        Rating: 10
        '''

        words = [imdb_link, review_title, review_text, rating]
        writer = csv.writer(out_file)
        writer.writerow(words)
        
        # break

out_file.close()

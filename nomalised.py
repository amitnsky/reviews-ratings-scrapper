
import csv


cur_dir = 'C:/Users/amit/Desktop/reviews-ratings-scrapper'

reviews_data = open(cur_dir + '/datasets/reviews.csv', 'r', newline='', encoding="utf-8")
dataset = open(cur_dir + '/datasets/dataset.csv', 'w', newline='', encoding="utf-8")

reviews_writer = csv.writer(dataset)
reviews_reader = csv.reader(reviews_data, delimiter=',')

# write index
words  = ['review_title', 'review', 'rating']
reviews_writer.writerow(words)

print("Dataset:")
k = 1

for line in reviews_reader:
    if k==1:
        k = k+1
        continue
    words = review_title, review_text, rating = line[1:4]
    reviews_writer.writerow(words)

    # print first 10 reviews, for verification
    if k<10:
        print("\n\nReview title: " + review_title
              + "\nReview text: " + review_text
              + "\nRating: " + rating)
    k=k+1

    '''
    output:
    Review title: The amount of people th...
    Review text: All the reviews that say ...
    Rating: 10
    '''
 

reviews_data.close()
dataset.close()


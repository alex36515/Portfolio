import pandas as pd
import re
from datetime import datetime
from dateutil import relativedelta
import os


unformatted_reviews = [[]]

with open('Data/reviews.txt', 'a', encoding="utf8") as f:
    line = f.readline()
    current_review = []
    # Iterate through the lines
    for next_line in f:
        # Checks if current line is equal to the next line
        if line == next_line:
            # Appends the reviewer values to the current_review list
            unformatted_reviews.append(current_review)
            current_review = []
            #inctiment next_line by 1 so next name is not at the end of current_review
            next_line = next(f)
        # append to current_review untill two (name) lines are equal
        current_review.append(line.rstrip())
        line = next_line


# combines the review text into one string
cleaned_review_text = ""
for review in unformatted_reviews:
    if len(review) > 5:
        for value in review[3:-1]:
            cleaned_review_text += value + " "
            review.pop(review.index(value))
        review.insert(3, cleaned_review_text)
        cleaned_review_text = ""




# Create a Pandas DataFrame from cleaned "unformatted_reviews"
df = pd.DataFrame(unformatted_reviews, columns=['name', 'reviewer_info', 'date_posted', 'revew_text', 'likes'])
df = df.dropna()

#reset the index
df = df.reset_index(drop=True)



#iderate through reviewer_info column and split the string into a list to distinguish reviewer status, num reviews, and num photos
reviewer_info_deliminated = []
for index, row in df['reviewer_info'].iteritems():

    reviewer_info_split = row.split('·')

    # initalises and resets the variables for each reviewer
    local_guide_info, review_count, photo_count = '', '', ''

    for info in reviewer_info_split:
        if re.findall("Local Guide", info):
            local_guide_info = info
        if re.findall("reviews", info):
            # removes the word "reviews" from the string
            review_count = info[0:-8]
        if re.findall("photos", info):
            # removes the word "photos" from the string
            photo_count = info[0:-7]
    reviewer_info_deliminated.append([[local_guide_info or ''], [review_count or '0'], [photo_count or '0']])


# Create a Pandas DataFrame from cleaned "reviewer_info_deliminated"
reviewer_info_df = pd.DataFrame(reviewer_info_deliminated, columns=['Status', 'review_count', 'photo_count'])

#replace the reviewer_info column with the new deliminated columns
df = df.drop('reviewer_info', axis=1)
df = df.join(reviewer_info_df)



# cleans the columns
df['likes'] = df['likes'].apply(lambda x: 0 if x == 'Like' else int(x))
df['Status'] = df['Status'].apply(lambda x: x[0])
df['review_count'] = df['review_count'].apply(lambda x: int(x[0]))
df['photo_count'] = df['photo_count'].apply(lambda x: int(x[0]))
df['date_posted'] = df['date_posted'].apply(lambda x: x.replace("NEW", ""))


# **unfinished** iterate through date_posted column with for loop
current_date = datetime(2023, 1, 1)
for index, row in df['date_posted'].iteritems():
    row = row.replace("NEW", "")
    #row = current_date - relativedelta.relativedelta(months=int(row.split()[0]))


print(df['revew_text'].head(50))
df['revew_text'].to_csv('review_text.csv', sep='\n', index=False)
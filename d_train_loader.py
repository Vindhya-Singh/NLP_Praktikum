# -*- coding: utf-8 -*-
"""d_train_loader.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zN9jgdAJGujwWJep1lPo2456ojFm7g-N

**Loading the k-core Data per Product Category **
"""

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

from google.colab import drive
drive.mount('/gdrive')

"""## Common Function to read the downloaded data in dataframes"""

import pandas as pd
import os
import gzip

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

"""## Data Frame for the Pet_Supplies Product category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Pet_Supplies_5.json.gz')
df.head()

"""## Data Frame for the Office Product category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Office_Products_5.json.gz')

df.head()

"""## Data Frame for the Musical Instruments  category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Musical_Instruments_5.json.gz')
df.head()

"""## Data Frame for the Patio, Lawn and Garden category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Patio_Lawn_and_Garden_5.json.gz')
df.head()

"""## Data Frame for the Baby_5 category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Baby_5.json.gz')
df.head()

"""## Data Frame for the Electronics category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Electronics_5.json.gz')
df.head()

"""## Data Frame for the Health and Personal Care category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Health_and_Personal_Care_5.json.gz')
df.head()

"""## Data Frame for the Beauty category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Beauty_5.json.gz')
df.head()

"""## Data Frame for the Cell Phones and Accessories category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Cell_Phones_and_Accessories_5.json.gz')
df.head()

"""## Data Frame for the Clothing, Jewelry and Shoes category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Clothing_Shoes_and_Jewelry_5.json.gz')
df.head()

"""## Data Frame for the Sports and Outdoors category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Sports_and_Outdoors_5.json.gz')
df.head()

"""## Data Frame for the Home and Kitchen category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Home_and_Kitchen_5.json.gz')
df.head()

"""## Data Frame for the Grocery and Gourmet Food category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Grocery_and_Gourmet_Food_5.json.gz')
df.head()

"""## Data Frame for the Automotive category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Automotive_5.json.gz')
df.head()

"""## Data Frame for the Amazon Instant Video category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Amazon_Instant_Video_5.json.gz')
df.head(100)

"""## Data Frame for the Digital Music category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Digital_Music_5.json.gz')
df.head()

"""## Data Frame for the Tools and Home Improvement category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Tools_and_Home_Improvement_5.json.gz')
df.head()
#df.columns

"""## Data Frame for the Books category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Books_5.json.gz')
df.head()

"""## Data Frame for the CDs and Vinylcategory"""

df = getDF('/gdrive/My Drive/d_training/reviews_CDs_and_Vinyl_5.json.gz')
df.head()

"""## Data Frame for the Kindle Store category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Kindle_Store_5.json.gz')
df.head()

"""## Data Frame for the Apps for Android category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Apps_for_Android_5.json.gz')
df.head()

"""## Data Frame for the Movies and TV category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Movies_and_TV_5.json.gz')
df.head()

"""## Data Frame for the Video_Games category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Video_Games_5.json.gz')
df.head()

"""## Data Frame for the Toys and Games category"""

df = getDF('/gdrive/My Drive/d_training/reviews_Toys_and_Games_5.json.gz')
df.head()

"""## Data Pre-processing"""

import numpy as np
import nltk
nltk.download('stopwords')
nltk.download('punkt')
import re  
from nltk.corpus import stopwords
stops1 = set(stopwords.words("english"))

train1 = pd.DataFrame(pd.concat([df['reviewerID'], df['reviewText'],df['overall'],df['summary']], axis=1))
train1.head()

def clean_sent(sent):
    sent = sent.lower()
    sent = re.sub(u'[_"\-;%()|+&=*%.,!?:#$@\[\]/]',' ',sent)
    return sent
def clean(df):
    df['reviewText'] = df.reviewText.map(lambda x: ' '.join([ word for word in
                                                         nltk.word_tokenize(clean_sent(x))]).encode('utf-8'))

    df['summary'] = df.summary.map(lambda x: ' '.join([ word for word in
                                                         nltk.word_tokenize(clean_sent(x))]).encode('utf-8'))
def removeStopWords(df, stop):
	df['reviewText'] = df.reviewText.map(lambda x: ' '.join([word for word in nltk.word_tokenize(x.decode('utf-8'))
                                                         if word not in stop]).encode('utf-8'))
	df['summary'] = df.summary.map(lambda x: ' '.join([word for word in nltk.word_tokenize(x.decode('utf-8'))
                                                         if word not in stop]).encode('utf-8'))

#Calling Clean and Stop words on Amazon Product data DF
clean(train1)
removeStopWords(train1, stops1)

#Calling out the pre-processed data frame named train1
train1.head()

"""## Converting all the Data Frames into respective CSVs per Product Category"""

df.to_csv(r'/gdrive/My Drive/test.csv', index=False, header=True)

df_100 = pd.read_csv('/gdrive/My Drive/test.csv', nrows = 100)
df_100.to_csv(r'/gdrive/My Drive/test_100_Books.csv', index=False, header=True)

df_100.head()

"""## Final Concatenation of all CSVs into one CSV with 100 samples per Product Category"""

#Concatenating all the csvs into a single dataframe per product category
import pandas as pd
import glob

path = r'/gdrive/My Drive' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

frame.head(200)

#Saving the final training data frame as a csv
frame.to_csv(r'/gdrive/My Drive/concatenated_100.csv', index=False, header=True)
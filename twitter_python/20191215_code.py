################## Set Environment ##################
import os
import pandas as pd
import tweepy
#conda install -c conda-forge tweepy

import textblob
from textblob import TextBlob
#conda install -c conda-forge textblob

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


Path = r'F:\Deependra\Data Scientist\001UAE\20191215_sentiment_analysis\twitter_python'
Path_Data = Path + '\Data'
Path_Output = Path + '\Output'

os.chdir(Path)

################## Start ##################

wiki =  TextBlob("Deependra is angry that he never gets good job")

wiki.tags
wiki.words
wiki.sentiment.polarity
wiki.sentiment_assessments

























'''
I want to become data scientist, whats to do some projects using tweeter sentimental analysis for UAE banking sector. 
Will extract customer feedback for top UAE banks like 
First abu dhabi bank
Emirates nbd
Abu dhabi commercial bank
Dubai islamic bank
Mashreq
HSBC UAE
'''
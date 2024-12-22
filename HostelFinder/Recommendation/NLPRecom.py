import nltk

import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from ast import literal_eval

# data = pd.read_csv("RecommendationDataSet.csv",names=["Hostel Address","Rating","Hostel Name","Tags","Locality"])
data=pd.read_csv(r"E:\Hostel-Finder\HostelFinder\Recommendation\RecommendationDataSet-3.csv")
data['Locality'] = data['Locality'].str.lower()
data['Tags'] = data['Tags'].str.lower()

def recommend_hotel(location, description):
    description = description.lower()
    word_tokenize(description)
    stop_words = stopwords.words('english')
    lemm = WordNetLemmatizer()
    filtered  = {word for word in description if not word in stop_words}
    filtered_set = set()
    for fs in filtered:
        filtered_set.add(lemm.lemmatize(fs))

    country = data[data['Locality']==location.lower()]
    country = country.set_index(np.arange(country.shape[0]))
    list1 = []; list2 = []; cos = [];
    for i in range(country.shape[0]):
        temp_token = word_tokenize(country["Tags"][i])
        temp_set = [word for word in temp_token if not word in stop_words]
        temp2_set = set()
        for s in temp_set:
            temp2_set.add(lemm.lemmatize(s))
        vector = temp2_set.intersection(filtered_set)
        cos.append(len(vector))
    country['similarity']=cos
    country = country.sort_values(by='similarity', ascending=True)
    # country.drop_duplicates(subset='Hostel_Name', keep='first', inplace=True)
    country.sort_values('rating', ascending=False, inplace=True)
    country.reset_index(inplace=True)
    return country[["Hostel_name", "rating", "Address"]]
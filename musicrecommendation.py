import numpy as np
import pandas as pd
import ast
import random
from face import *
songs=pd.read_csv('top50MusicFrom2010-2019.csv')
a=pd.read_csv('top50MusicFrom2010-2019.csv')
# title
# genres
songs=songs[['artist','title','genre','year','Beats']]
songs.dropna(inplace=True)
songs.isnull().sum()
songs.duplicated().sum()
songs.iloc[1].genre

def con(obj):
    c=[]
    l=str(obj)
    for i in l:
        c.append(i)
    return c
def con2(obj):
    c=obj.split(" ")
    return c
def con3(obj):
    c="".join(obj)
    c=c.split(" ")
    return c

songs['year']=songs['year'].apply(con)
songs['Beats']=(songs['Beats']).apply(con)


songs['genre']=songs['genre'].apply(con2)
songs['genre']=songs['genre'].apply(lambda x:[i.replace(" ","")for i in x])

songs['artist']=songs['artist'].apply(con3)

#print(songs['artist'].head())


songs['tags']=songs['artist'] + songs['genre'] + songs['year'] + songs['Beats']







new_df=songs[['title','tags']]
new_df['tags']=new_df['tags'].apply(lambda x:" ".join(x))
new_df['tags']=new_df['tags'].apply(lambda x:x.lower())
new_df['title']=new_df['title'].apply(lambda x:x.lower())

#print(new_df['tags'][1])



from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=350)
vectors=cv.fit_transform(new_df['tags']).toarray()
#print(vectors.shape)
from sklearn.metrics.pairwise import cosine_similarity
similarity=cosine_similarity(vectors)
#print(similarity.shape)
#...............................Main function.........................
#print(new_df[new_df['title']=='TiK ToK'].index[0])

def recommend(songs):
    start=random.randint(3,20)
    last=random.randint(20,35)
    song_index=new_df[new_df['title']==songs].index[0]
    distances=similarity[song_index]
    if start<last:
        song_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[start:last+5]
    elif start==last:
        last=start+10
        song_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[start:last]
    for i in song_list:
        print(new_df.iloc[i[0]].title)

#....................................Based on mood....................................

songs['mood']=songs['genre']
new_df1=songs[['title','mood']]
new_df1['mood']=new_df1['mood'].apply(lambda x:" ".join(x))
new_df1['mood']=new_df1['mood'].apply(lambda x:x.lower())
from sklearn.feature_extraction.text import CountVectorizer
cv1=CountVectorizer(max_features=55)
vectors1=cv1.fit_transform(new_df1['mood']).toarray()
#print(vectors1.shape)
from sklearn.metrics.pairwise import cosine_similarity
similarity1=cosine_similarity(vectors1)

def recommend_on_mood(mood):
    start=random.randint(3,20)
    last=random.randint(20,35)
    song_index=new_df1[new_df1['mood']==mood].index[0]
    distances=similarity[song_index]
    if start<last:
        song_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[start:last]
    elif start==last:
        last=start+10
        song_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[start:last]
    for i in song_list:
        print(new_df1.iloc[i[0]].title)

def play_on_mood(mood):
    mood=mood.lower()
    if mood=='happy':
        recommend_on_mood('dance pop')
    elif mood=='sad':
        recommend_on_mood('hip hop') or recommend_on_mood('celtic rock')
    elif mood=='fear':
        recommend_on_mood('hip hop') or recommend_on_mood('celtic rock')
    elif mood=='surprise':
        recommend_on_mood('electropop')



l=[]
for i in a['title']:
    l.append(i.lower())
print(new_df1)

import pickle
pickle.dump(new_df.to_dict(),open('musics_dict.pkl','wb'))
pickle.dump(new_df1.to_dict(),open('musics_dict1.pkl','wb'))

pickle.dump(similarity,open('similarity.pkl','wb'))
pickle.dump(similarity1,open('similarity1.pkl','wb'))


while True:
    print("Enter 1 to play on mood base ")
    print("Enter 2 to play on mood base using camera ")
    print("Enter 3 for Suggest on your current song ")
    x=input(" ")
    if x=='1':
        m=input("Enter Your mood ")
        play_on_mood(m)
    elif x=='3':
        s=input("Enter your song name ").lower()
        if s in l:
            recommend(s)
        else:
            print("Selected song is not in Databasse") 
    elif x=='2':
        m=recog()
        play_on_mood(m)
    else:
        print("Adios ")
        exit()



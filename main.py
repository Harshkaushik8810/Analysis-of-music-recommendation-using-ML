import streamlit as st
import pickle
import pandas as pd
import random
import os
from face import recog
def recommend(option):
    start=random.randint(3,20)
    last=random.randint(20,35)
    song_index=music[music['title']==option].index[0]
    distances=similarity[song_index]
    if start<last:
        song_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[start:last+5]
    elif start==last:
        last=start+10
        song_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[start:last]
    recommended_song=[]
    for i in song_list:
        recommended_song.append(music.iloc[i[0]].title)
    return recommended_song


def recommend_on_mood(option1):
    if option1=='happy':
        mood='dance pop'
    elif option1=='sad':
        mood='hip hop' or 'celtic rock'
    elif option1=='surprise':
        mood='electropop'
    elif option1=='neutral':
        mood='hip hop' or 'celtic rock' or 'electropop' or 'dance pop'
    else:
        st.write("Try again")
    start=random.randint(3,20)
    last=random.randint(20,35)
    song_index=music1[music1['mood']==mood].index[0]
    distances=similarity[song_index]
    if start<last:
        song_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[start:last]
    elif start==last:
        last=start+10
        song_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[start:last]
    recommended_song1=[]
    for i in song_list:
        recommended_song1.append(music.iloc[i[0]].title)
    return recommended_song1







music_list=pickle.load(open('musics_dict.pkl','rb'))

music=pd.DataFrame(music_list)

music_list1=pickle.load(open('musics_dict1.pkl','rb'))

music1=pd.DataFrame(music_list1)

similarity=pickle.load(open('similarity.pkl','rb'))

similarity1=pickle.load(open('similarity1.pkl','rb'))

st.title('Music Recommendation System')
option=st.selectbox('Select a music',music['title'].values)

option1=st.selectbox('Select a mood',('happy','sad','surprise','neutral'))

c1,c2,c3=st.columns(3)
with c1:
    if st.button('Recommend on mood'):
        recommendation1=recommend_on_mood(option1)
        j=1
        for i in recommendation1:
            st.write(j,i)
            j=j+1
with c2:
    if st.button('Recommend on music'):
        recommendation=recommend(option)
        j=1
        for i in recommendation:
            st.write(j,i)
            j=j+1
with c3:
    if st.button('Recommend using Face expression'):
        mood=recog()
        st.write(f'Your mood is {mood}')
        recommendation=recommend_on_mood(mood)
        j=1
        for i in recommendation:
            st.write(j,i)
            j=j+1





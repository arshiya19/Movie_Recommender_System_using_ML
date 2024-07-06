import streamlit as st
import pickle 

movies_list = pickle.load(open('movues.pkl','rb'))
movies_list = movies_list['title'].values
st.title('Movies')

option = st.selectbox( 'What would like to search?', movies_list )

option = st.selectbox( 'What would like to search?', movies_list )




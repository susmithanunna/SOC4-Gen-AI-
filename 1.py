import streamlit as st #streamlit is package in python used to create  UI
st.set_page_config(page_title='Foodie')
st.header("Tyoes of Foodies")
col1,col2=st.columns(2)
with col1:
  st.subheader("Shinchan ")
  st.image("https://media4.giphy.com/media/12Yug01me26oH6/giphy.gif",caption="Cute Eater",width=300,use_column_width=True)
  st.write("Cute Eater Shinchana")
with col2:
    st.subheader("Duck")
    st.image("https://media.tenor.com/AFagQ7fK8JUAAAAj/food-yummy.gif",caption="Fast Eater", width=300,use_column_width=True)
    st.write("Fast eater Duck")
    

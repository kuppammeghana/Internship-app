import streamlit as st 

st.title(':blue[Hello Everyone!] :star-struck:')
st.subheader("I am K. Meghana")
st.title("A Data Science Student")
st.write('I am enthusiastic in the field of data science. I am currently working as a data science intern at Innomatics Research Labs. I would like to be in discussions involving this field. ')
st.write('Have a look at interactive Dashboards of Iris and Titanic dataset')
st.write("Let's Connect!")
button1=st.button('LinkedIn')
if button1==True:
    st.write('https://www.linkedin.com/in/kuppam-meghana-945474259')
button2=st.button('GitHub')
if button2==True:
    st.write('https://github.com/kuppammeghana')

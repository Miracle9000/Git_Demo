import streamlit as st

st.write("hello world")
movie = st.text_input("Fav Movie?")
st.write(f"So your best movie is {movie}")
is_clicked = st.button("Click Me")
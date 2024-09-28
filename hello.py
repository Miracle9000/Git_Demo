import streamlit as st

#st.write("hello world")
#movie = st.text_input("Fav Movie?")
#st.write(f"So your best movie is {movie}")
#is_clicked = st.button("Click Me")

import streamlit as st

def main():
    st.title("AI Text Generator")

    prompt = st.text_input("Enter your prompt:")

    if st.button("Generate"):
        # Replace this with your actual AI processing logic
        response = "This is a generated response based on your prompt."

        st.text_area("Response:", value=response, height=200)

if __name__ == "__main__":
    main()

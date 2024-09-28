import streamlit as st

#st.write("hello world")
#movie = st.text_input("Fav Movie?")
#st.write(f"So your best movie is {movie}")
#is_clicked = st.button("Click Me")

def main():
    st.title("AI Text Generator")

    st.markdown(
        """
        <style>
        .st-bb {
            background-color: #000000;
            border-radius: 10px;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    with st.form("my_form"):
        
        prompt = st.text_input("Enter your prompt:")
        #prompt = st.text_input("Enter your prompt:", class_="st-bb")
        #prompt = st.markdown("<span style='color: blue;'>Enter your prompt:</span>", unsafe_allow_html=True)
        submit_button = st.form_submit_button("Generate")

    if submit_button:
        # Replace this with your actual AI processing logic
        response = "This is a generated response based on your prompt."

        st.markdown(
            f"""
            <div class="st-bb">
                {response}
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()

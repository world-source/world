import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
s = f"<p style='font-size:20px;'>{Hi}</p>"
st.markdown(s, unsafe_allow_html=True) 

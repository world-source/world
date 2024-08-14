import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
label = "Enter text here"
st.text_input(Hello)

st.components.v1.html(
    f"""
    <script>
        var elems = window.parent.document.querySelectorAll('div[class*="stTextInput"] p');
        var elem = Array.from(elems).find(x => x.innerText == '{Hello}');
        elem.style.fontSize = '20px'; // the fontsize you want to set it to
    </script>
    """
)

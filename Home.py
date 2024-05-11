import streamlit as st
import pandas

st.set_page_config(layout="wide", page_title="Mahd")
col1, col2 = st.columns(2)


page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: linear-gradient( 111.4deg,  rgba(7,7,9,1) 6.5%, rgba(27,24,113,1) 93.2% );}
<style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("""
<style>
@keyframes slideInFromLeft {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(0);
  }
}
.slide-in-left {
  animation: 1s ease-out 0s 1 slideInFromLeft;
}

</style>
""", unsafe_allow_html=True)

with col1:
    st.image("pictures/me.jpg")

with col2:
    st.markdown("<h1 class='slide-in-left'> Mahdi Meyghani</h1>",
                unsafe_allow_html=True)
    st.write("""<font size='+4'><p class='slide-in-left'>Hello there! 👋 
    I'm Mahdi, 
    I'm a Python programmer focusing on backend. 
    I spend most of my time working with awesome technologies like 
    Django, Docker, SQL databases, etc. 
    I love collaborating with teams and I'm always excited to 
    learn and adapt to new tech! Below, you can find some of the cool Apps 
    I have built in Python. Feel free to contact me !</font></p>""",
             unsafe_allow_html=True)

    st.image("pictures/arrow.png")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        title = row["title"]
        st.markdown(f"<h1 class='slide-in-left'>{title}</h1>",
                    unsafe_allow_html=True)

        description = row["description"]
        st.markdown(f"<p class='slide-in-left'>{description}</p>",
                    unsafe_allow_html=True)

        image = "pictures/" + row["image"]
        st.image(image)

        link = row["url"]
        st.write(f"[Source Code]({link})")

with col4:
    for index, row in df[10:].iterrows():
        title = row["title"]
        st.markdown(f"<h1 class='slide-in-left'>{title}</h1>",
                    unsafe_allow_html=True)

        description = row["description"]
        st.markdown(f"<p class='slide-in-left'>{description}</p>",
                    unsafe_allow_html=True)

        image = "pictures/" + row["image"]
        st.image(image)

        link = row["url"]
        st.write(f"[Source Code]({link})")

st.write("[Click for more...](https://github.com/Mahdi-Meyghani)")
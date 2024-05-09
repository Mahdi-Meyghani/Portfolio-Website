import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# background-image: linear-gradient( 179.7deg,  rgba(249,21,215,1) 1.1%, rgba(22,0,98,1) 99% );
# background-image: linear-gradient( 85.2deg,  rgba(33,3,40,1) 7.5%, rgba(65,5,72,1) 88.7% );

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
.big-font {
    font-size:20px !important;
    height: 1px;
}
</style>
""", unsafe_allow_html=True)

with col1:
    st.image("me.jpg")

with col2:
    st.markdown("<h1 class='slide-in-left'> Mahdi Meyghani</h1>",
                unsafe_allow_html=True)

    # st.markdown("""<p class="big-font slide-in-left">Hi, I am Mahdi.
    # I am a Python programmer focusing on backend.
    # I also have a background in graphics, but it doesn't matter because right now
    # my passion and all my time is spent on technology, anyway below you can find
    # some of the Apps
    # i have built in Python, Feel free to contact me !</p>""",
    #             unsafe_allow_html=True)

    # st.text_area("""Hi, I am Mahdi. I am a Python programmer focusing on backend.
    # I also have a background in graphics, but it doesn't matter because right now
    # my passion and all my time is spent on technology, anyway,
    # below you can see some of my projects.""", height=200)

    # content = """Hi, I am Mahdi. I am a Python programmer focusing on backend.
    # I also have a background in graphics, but it doesn't matter because right now
    # my passion and all my time is spent on technology, anyway,
    # below you can see some of my projects."""
    # st.info(content)

    st.write("""<font size='+5'>Hi, I am Mahdi.
    I am a Python programmer focusing on backend.
    I also have a background in graphics, but it doesn't matter because right now
    my passion and all my time is spent on technology, anyway below you can find
    some of the Apps
    i have built in Python, Feel free to contact me !</font>""", unsafe_allow_html=True)
with col3:
    st.markdown("<h1 class='slide-in-left'> To Do App</h1>",
                unsafe_allow_html=True)

    st.write("""A distraction-free web app
    to help you focus on your goals :)""", )

    st.image("1.png")

    st.write("[Source Code](https://github.com/Mahdi-Meyghani)")
    # --------------------------------------------------------------------------
    st.markdown("<h1 class='slide-in-left'> To Do App</h1>",
                unsafe_allow_html=True)

    st.write("""A distraction-free web app
    to help you focus on your goals :)""", )

    st.image("1.png")

    st.write("[Source Code](https://github.com/Mahdi-Meyghani)")

with col4:
    st.markdown("<h1 class='slide-in-left'> Portfolio Website</h1>",
                unsafe_allow_html=True)

    st.write("""A portfolio website built
    entirely in Python to showcase coding projects.""")

    st.image("2.png")

    st.write("[Source code](https://github.com/Mahdi-Meyghani)")
    # --------------------------------------------------------------------------
    st.markdown("<h1 class='slide-in-left'> Portfolio Website</h1>",
                unsafe_allow_html=True)

    st.write("""A portfolio website built
    entirely in Python to showcase coding projects.""")

    st.image("2.png")

    st.write("[Source code](https://github.com/Mahdi-Meyghani)")

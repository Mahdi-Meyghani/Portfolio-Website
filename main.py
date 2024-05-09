import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

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

    st.markdown("""<p class="big-font slide-in-left">Hi, I am Mahdi.
    I am a Python programmer focusing on backend.
    I also have a background in graphics, but it doesn't matter because right now
    my passion and all my time is spent on technology, anyway below you can find
    some of the Apps
    i have built in Python, Feel free to contact me !</p>""",
                unsafe_allow_html=True)

    # st.text_area("""Hi, I am Mahdi. I am a Python programmer focusing on backend.
    # I also have a background in graphics, but it doesn't matter because right now
    # my passion and all my time is spent on technology, anyway,
    # below you can see some of my projects.""", height=200)

    # content = """Hi, I am Mahdi. I am a Python programmer focusing on backend.
    # I also have a background in graphics, but it doesn't matter because right now
    # my passion and all my time is spent on technology, anyway,
    # below you can see some of my projects."""
    # st.info(content)

    # st.write("""<p class="big-font slide-in-left">Hi, I am Mahdi. I am a Python programmer focusing on backend.
    # I also have a background in graphics, but it doesn't matter because right now
    # my passion and all my time is spent on technology, anyway,
    # below you can see some of my projects.</p>""", unsafe_allow_html=True)
with col3:
    st.markdown("<h1 class='slide-in-left'> To Do App</h1>",
                unsafe_allow_html=True)

    st.markdown("""<p class="big-font slide-in-left">A distraction-free web app
    to help you focus on your goals :)</p>""",
                unsafe_allow_html=True)

    st.image("1.png")

    st.write("<a href='#' id='https://github.com/Mahdi-Meyghani/ToDo-Web-App'>"
             "Source Code</a>", unsafe_allow_html=True)
    # --------------------------------------------------------------------------
    st.markdown("<h1 class='slide-in-left'> To Do App</h1>",
                unsafe_allow_html=True)

    st.markdown("""<p class="big-font slide-in-left">A distraction-free web app
    to help you focus on your goals :)</p>""",
                unsafe_allow_html=True)

    st.image("1.png")

    st.write("<a href='#' id='https://github.com/Mahdi-Meyghani/ToDo-Web-App'>"
             "Source Code</a>", unsafe_allow_html=True)

with col4:
    st.markdown("<h1 class='slide-in-left'> Portfolio Website</h1>",
                unsafe_allow_html=True)

    st.markdown("""<p class="big-font slide-in-left">A portfolio website built
    entirely in Python to showcase coding projects.</p>""",
                unsafe_allow_html=True)

    st.image("2.png")

    st.write("<a href='#' id='https://github.com/Mahdi-Meyghani/ToDo-Web-App'>"
             "Source Code</a>", unsafe_allow_html=True)
    # --------------------------------------------------------------------------
    st.markdown("<h1 class='slide-in-left'> Portfolio Website</h1>",
                unsafe_allow_html=True)

    st.markdown("""<p class="big-font slide-in-left">A portfolio website built
    entirely in Python to showcase coding projects.</p>""",
                unsafe_allow_html=True)

    st.image("2.png")

    st.write("<a href='#' id='https://github.com/Mahdi-Meyghani/ToDo-Web-App'>"
             "Source Code</a>", unsafe_allow_html=True)


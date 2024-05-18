import streamlit as st
import sending_email
import requests

st.set_page_config(layout="wide")
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

st.markdown("<h1 class='slide-in-left'> Contact Me</h1>",
            unsafe_allow_html=True)

with st.form(key="form"):
    user_email = st.text_input("Enter Your Email Address:",
                               placeholder=" example@email.com")

    message_email = st.text_area("Enter Your Message:", placeholder="Your Message")

    submit_button = st.form_submit_button("Submit")

    if submit_button:
        if user_email and message_email:

            sending_email.send_email(email_address=user_email,
                                     message=message_email)

            st.write("<p class='slide-in-left' style='color: green'>"
                     "Email sent successfully !</p>",
                     unsafe_allow_html=True)

        else:
            st.write("<p class='slide-in-left' style='color: red'>"
                     "Fill the BOXES first !</p>",
                     unsafe_allow_html=True)


# Get the API content
API_KEY = "1VN1PYKrNZpb6NIW71gfgvAPgXJyi9Fko1J4oweV"

response = requests.get("https://api.nasa.gov/"
                        "planetary/"
                        "apod?"
                        f"api_key={API_KEY}")


content = response.json()

title = content["title"]
description = content["explanation"]
image_url = content["url"]
date = content["date"]

# Create streamlit page
st.markdown(f"<h1 class='slide-in-left'>Astronomy Picture Of The Day</h1>",
            unsafe_allow_html=True)

st.write("<p class='slide-in-left'>This is the "
         "Astronomy Picture Of the day by NASA's official website, "
         "which is updated daily. :)</p>",
         unsafe_allow_html=True)

st.markdown(f"<h2 class='slide-in-left'>{title}</h2>",
            unsafe_allow_html=True)

st.image(image_url)

st.write(f"<p class='slide-in-left'>{description}</p>",
         unsafe_allow_html=True)

st.subheader(date)

from PIL import Image
import streamlit as st
import json
from streamlit_lottie import st_lottie

st.set_page_config(page_title="CodeXploit", page_icon="☣", layout="wide")


def loadLottieFile(filepath: str):
    with open(filepath, "r") as file:
        return json.load(file)


def local_css(file_name):
    with open(file_name) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)


lottie_coding1 = loadLottieFile("coding2.json")
lottie_coding2 = loadLottieFile("coding1.json")
image = Image.open("images/image.png")

#  --- HEADER SECTION -----
with st.container():
    st.subheader("Hi, I am Aryan Kumar Upadhyay :wave:")
    st.title("A Python Developer From India")
    st.write("I specialize in designing elegant user interfaces and implementing efficient backend solutions using "
             "Django")
    st.write("[Hire Me >](https://www.fiverr.com/mark_aryan)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            1. UI/UX Design:
            Captivate your audience with visually appealing and user-centric design. I craft intuitive user interfaces 
            and seamless user experiences that engage and retain your customers.
            
            2. Web Development:
            Transform your ideas into fully functional websites. From e-commerce platforms to informative corporate 
            sites, I create web solutions that align perfectly with your business goals.
            
            3. Web Designing:
            Enhance your online presence with custom web designs that reflect your brand's personality. I create designs
             that not only look great but also convert visitors into loyal customers.
            
            4. Digital Marketing:
            Navigate the complex world of digital marketing with confidence. I devise tailored strategies encompassing 
            SEO, social media, and content marketing to increase your brand's visibility and drive growth.
            
            5. Training:
            Empower your team with the knowledge and skills needed to excel in today's competitive landscape. I provide 
            training sessions that cover various aspects of design, development, and digital marketing.
            
            Python Programming Expertise:
            As a proficient Python programmer, I harness the power of cutting-edge modules to bring efficiency and 
            innovation to your projects.
            
            Empowering startups with affordability, innovation, and expertise.
            """
        )
        st.write("[Personal Website >](https://codexploit.com)")
    with right_column:
        st_lottie(
            lottie_coding1,
            speed=1,
            reverse=False,
            loop=True,
            quality="low",
            height=None,
            width=None,
            key=None
        )

#  ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image)
    with text_column:
        st.subheader("Created a ChatApp!")
        st.write(
            """
            Created a chat app, designed by Figma and developed py Wordpress.
            It includes:-
            1. SEO
            2. Content Marketing
            3. Call To Actions 
            4. Contact Form 
            5. Illustrations
            and many more
            """
        )
        st.markdown("[Comming Soon...](https://codexploit.com/project/3)")

# --- CONTACT SECTION ---
with st.container():
    st.write("---")
    st.header(":mailbox: Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/xyzmark00@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" placeholder="Enter your name" name="name" required>
         <input type="email" placeholder="Enter your email" name="email" required>
         <textarea name="message" placeholder="Details of your problem" rows="5" ></textarea>
         <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns((2,1))
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

    with right_column:
        st_lottie(
            lottie_coding2,
            speed=1,
            reverse=False,
            loop=True,
            quality="low",
            height=None,
            width=350,
            key=None
        )

    local_css("style/style.css")

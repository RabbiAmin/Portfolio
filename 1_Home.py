import streamlit as st
from PIL import Image
import requests
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from constant import *
from streamlit_lottie import st_lottie
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
import openai
from langchain.chat_models import ChatOpenAI


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(
    page_title="Amin Webpage",
    page_icon=":tada:",
    layout="wide")

# -----------------  chatbot  ----------------- #
# # Set up the OpenAI key
# openai_api_key = st.sidebar.text_input('Enter your OpenAI API Key and hit Enter', type="password")
# openai.api_key = (openai_api_key)

# Add Google AdSense
adsense_code = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5062604894981545"
     crossorigin="anonymous"></script>
"""
components.html(adsense_code, height=0)  # height=0 since it doesn't have direct visual content


# load the file
documents = SimpleDirectoryReader(input_files=["bio.txt"]).load_data()
#documents = SimpleDirectoryReader("bio.txt").load_data()




pronoun = info["Pronoun"]
name = info["Name"]
# def ask_bot(input_text):
#     # define LLM
#     llm = ChatOpenAI(
#         model_name="gpt-3.5-turbo",
#         temperature=0,
#         openai_api_key=openai.api_key,
#     )
#     llm_predictor = LLMPredictor(llm=llm)
#     service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
#
#     # load index
#     index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
#
#     # query LlamaIndex and GPT-3.5 for the AI's response
#     PROMPT_QUESTION = f"""You are Buddy, an AI assistant dedicated to assisting {name} in her job search by providing recruiters with relevant and concise information.
#     If you do not know the answer, politely admit it and let recruiters know how to contact {name} to get more information directly from {pronoun}.
#     Don't put "Buddy" or a breakline in the front of your answer.
#     Human: {input_text}
#     """
#
#
#     output = index.as_query_engine().query(PROMPT_QUESTION.format(input=input_text))
#     print(f"output: {output}")
#     return output.response




# get the user's input by calling the get_text function
# def get_text():
#     input_text = st.text_input("After providing OpenAI API Key on the sidebar, you can send your questions and hit Enter to know more about me from my AI agent, Buddy!", key="input")
#     return input_text
#
# #st.markdown("Chat With Me Now")
# user_input = get_text()
#
# if user_input:
#   #text = st.text_area('Enter your questions')
#   if not openai_api_key.startswith('sk-'):
#     st.warning('⚠️Please enter your OpenAI API key on the sidebar.', icon='⚠')
#   if openai_api_key.startswith('sk-'):
#     st.info(ask_bot(user_input))

# -----------------  loading assets  ----------------- #
st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

def apply_css_filters(lottie_url, filter_style):
    lottie_html = f"""
    <div style="filter: {filter_style};">
        <script src="{lottie_url}"></script>
    </div>
    """
    components.html(lottie_html, height=300)

# Example of applying filters
apply_css_filters("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json", "brightness(1.5) contrast(1.2)")

# loading assets
lottie_gif = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
r_lottie = load_lottieurl("https://lottie.host/f5417bd0-7cdb-46ee-816d-5cd18b76817a/sglAAWVwJV.json")
robo_lottie = load_lottieurl("https://lottie.host/41a87b60-a1b8-4fbd-a28a-7a25e94ef80e/wSPoKxcM4E.json")
git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
mongodb_lottie = load_lottieurl("https://lottie.host/02eeadc0-1b96-4709-95f9-c28d6841608e/vzj1vCd69k.json")
linux_lottie = load_lottieurl("https://lottie.host/359a71c2-d6b3-473d-a34f-fcef11de3cde/DOta7EGFyk.json")
analysis_lottie = load_lottieurl("https://lottie.host/cb1c6c49-9df2-42d6-b1e8-835a667cda24/3TiAFbU32N.json")



# ----------------- info ----------------- #



def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'''
    <style>
        .gradient-header {{
            text-align: center;
            background-image: linear-gradient(to right, {color2}, {color1});    
            font-size: 40px;
            border-radius: 50%;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5); 
            transition: all 0.3s ease-in-out;
            color: {color3}; 
            padding: 20px; 
        }}
        .gradient-header:hover {{
            background-image: linear-gradient(to left, {color2}, {color1});
        }}
        @keyframes gradient-animation {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}
        .animated-gradient {{
            background-size: 200% 200%;
            animation: gradient-animation 15s ease infinite;
        }}
    </style>
    <h1 class="gradient-header animated-gradient">
        <span>{content1}</span><br>
        <span style="font-size: 15px;">{content2}</span>
    </h1>
    ''', unsafe_allow_html=True)




with st.container():
    col1, col2 = st.columns([8,0.001])

full_name = info['Full_Name']
with col1:
    gradient('#5A4692','#3097BF','#DADBDD',f"Hi, I'm {full_name}👋", info["Intro"])
    st.write("")
    st.markdown(
        f"<p style='font-size: 18px; color: #333; text-align: justify; line-height: 1.5em;'>{info['About']}</p>",
        unsafe_allow_html=True
    )

    
    
# with col2:
#     st_lottie(lottie_gif, height=280, key="data")


# ----------------- skillset ----------------- #
with st.container():
    # Apply the custom class for the skillset section
    st.markdown('<div class="skillset-section">', unsafe_allow_html=True)

    st.subheader('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=70, width=70, key="python", speed=1)
    with col2:
        st_lottie(r_lottie, height=70, width=70, key="r", speed=1)
    with col3:
        st_lottie(robo_lottie, height=70, width=70, key="robo", speed=1)
    with col4:
        st_lottie(git_lottie, height=70, width=70, key="git", speed=1)
    with col1:
        st_lottie(github_lottie, height=70, width=70, key="github", speed=1)
    with col2:
        st_lottie(mongodb_lottie, height=70, width=70, key="mongo", speed=1)
    with col3:
        st_lottie(linux_lottie, height=70, width=70, key="linux", speed=1)
    with col4:
        st_lottie(analysis_lottie, height=70, width=70, key="analysis", speed=1)

    # Close the div tag for the custom section
    st.markdown('</div>', unsafe_allow_html=True)



    
    
# ----------------- timeline ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('📌 Career Snapshot')

    # load data
    with open('example.json', "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=500)

# ----------- powerBI Renovation -----------#
img_1 = Image.open("images/image1.jpg")
img_2 = Image.open("images/image2.JPG")
img_3 = Image.open("images/image3.JPG")

with st.container():
    st.markdown("""""")
    st.subheader("📊 PowerBI")
    col1,col2 = st.columns([0.95, 0.05])
    # In the first column (col1)
    with col1:
        with st.expander('See the work'):
            st.subheader("")
        # Embed an HTML component to display the slideshow
            components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Styles for the slideshow -->
        <style>
            * {{box-sizing: border-box;}}
            .mySlides {{display: none;}}
            img {{vertical-align: middle;}}

            /* Slideshow container */
            .slideshow-container {{
            position: relative;
            margin: auto;
            width: 100%;
            }}

            /* The dots/bullets/indicators */
            .dot {{
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #eaeaea;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
            }}

            .active {{
            background-color: #6F6F6F;
            }}

            /* Fading animation */
            .fade {{
            animation-name: fade;
            animation-duration: 1s;
            }}

            @keyframes fade {{
            from {{opacity: .4}} 
            to {{opacity: 1}}
            }}

            /* On smaller screens, decrease text size */
            @media only screen and (max-width: 300px) {{
            .text {{font-size: 11px}}
            }}
            </style>
        </head>
        <body>
            <!-- Slideshow container -->
            <div class="slideshow-container">
                <div class="mySlides fade">
                <img src={img_1} style="width:100%">
                </div>

                <div class="mySlides fade">
                <img src={img_2} style="width:100%">
                </div>

                <div class="mySlides fade">
                <img src={img_3} style="width:100%">
                </div>

            </div>
            <br>
            <!-- Navigation dots -->
            <div style="text-align:center">
                <span class="dot"></span> 
                <span class="dot"></span> 
                <span class="dot"></span> 
            </div>

            <script>
            let slideIndex = 0;
            showSlides();

            function showSlides() {{
            let i;
            let slides = document.getElementsByClassName("mySlides");
            let dots = document.getElementsByClassName("dot");
            for (i = 0; i < slides.length; i++) {{
                slides[i].style.display = "none";  
            }}
            slideIndex++;
            if (slideIndex > slides.length) {{slideIndex = 1}}    
            for (i = 0; i < dots.length; i++) {{
                dots[i].className = dots[i].className.replace("active", "");
            }}
            slides[slideIndex-1].style.display = "block";  
            dots[slideIndex-1].className += " active";
            }}

            var interval = setInterval(showSlides, 2500); // Change image every 2.5 seconds

            function pauseSlides(event)
            {{
                clearInterval(interval); // Clear the interval we set earlier
            }}
            function resumeSlides(event)
            {{
                interval = setInterval(showSlides, 2500);
            }}
            // Set up event listeners for the mySlides
            var mySlides = document.getElementsByClassName("mySlides");
            for (i = 0; i < mySlides.length; i++) {{
            mySlides[i].onmouseover = pauseSlides;
            mySlides[i].onmouseout = resumeSlides;
            }}
            </script>

            </body>
            </html> 

            """,
                height=270,
)


# ----------------- medium ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('✍️ Medium')
    col1,col2 = st.columns([0.95, 0.05])
    with col1:
        with st.expander('Display my latest posts'):
            components.html(embed_rss['rss'],height=300)
            
            st.markdown(""" <a href={}> <em>🔗 access to the link </a>""".format(info['Medium']), unsafe_allow_html=True)

# -----------------  endorsement  ----------------- #
with st.container():
    # Divide the container into three columns
    col1,col2,col3 = st.columns([0.475, 0.475, 0.05])
    # In the first column (col1)        
    with col1:
        # Add a subheader to introduce the coworker endorsement slideshow
        st.subheader("👄 Coworker Endorsements")
        # Embed an HTML component to display the slideshow
        components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Styles for the slideshow -->
        <style>
            * {{box-sizing: border-box;}}
            .mySlides {{display: none;}}
            img {{vertical-align: middle;}}

            /* Slideshow container */
            .slideshow-container {{
            position: relative;
            margin: auto;
            width: 100%;
            }}

            /* The dots/bullets/indicators */
            .dot {{
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #eaeaea;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
            }}

            .active {{
            background-color: #6F6F6F;
            }}

            /* Fading animation */
            .fade {{
            animation-name: fade;
            animation-duration: 1s;
            }}

            @keyframes fade {{
            from {{opacity: .4}} 
            to {{opacity: 1}}
            }}

            /* On smaller screens, decrease text size */
            @media only screen and (max-width: 300px) {{
            .text {{font-size: 11px}}
            }}
            </style>
        </head>
        <body>
            <!-- Slideshow container -->
            <div class="slideshow-container">
                <div class="mySlides fade">
                <img src={endorsements["img1"]} style="width:100%">
                </div>

                <div class="mySlides fade">
                <img src={endorsements["img2"]} style="width:100%">
                </div>

                <div class="mySlides fade">
                <img src={endorsements["img3"]} style="width:100%">
                </div>

            </div>
            <br>
            <!-- Navigation dots -->
            <div style="text-align:center">
                <span class="dot"></span> 
                <span class="dot"></span> 
                <span class="dot"></span> 
            </div>

            <script>
            let slideIndex = 0;
            showSlides();

            function showSlides() {{
            let i;
            let slides = document.getElementsByClassName("mySlides");
            let dots = document.getElementsByClassName("dot");
            for (i = 0; i < slides.length; i++) {{
                slides[i].style.display = "none";  
            }}
            slideIndex++;
            if (slideIndex > slides.length) {{slideIndex = 1}}    
            for (i = 0; i < dots.length; i++) {{
                dots[i].className = dots[i].className.replace("active", "");
            }}
            slides[slideIndex-1].style.display = "block";  
            dots[slideIndex-1].className += " active";
            }}

            var interval = setInterval(showSlides, 2500); // Change image every 2.5 seconds

            function pauseSlides(event)
            {{
                clearInterval(interval); // Clear the interval we set earlier
            }}
            function resumeSlides(event)
            {{
                interval = setInterval(showSlides, 2500);
            }}
            // Set up event listeners for the mySlides
            var mySlides = document.getElementsByClassName("mySlides");
            for (i = 0; i < mySlides.length; i++) {{
            mySlides[i].onmouseover = pauseSlides;
            mySlides[i].onmouseout = resumeSlides;
            }}
            </script>

            </body>
            </html> 

            """,
                height=270,
    )  

# -----------------  contact  ----------------- #
    with col2:
        st.subheader("📨 Contact Me")
        contact_form = f"""
        <form action="https://formsubmit.co/{info["Email"]}" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

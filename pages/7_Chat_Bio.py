import spacy

nlp = spacy.load("en_core_web_sm")


import streamlit as st

st.title("Resume Chatbot with NLP")

# Define the content of your resume or bio file
resume_content = """
About Md. Rabbi Amin:
Md. Rabbi Amin is an accomplished Data Analyst with a strong academic background and a passion for emerging technologies. He holds a BSc in Computer Science and Engineering from North South University and is currently pursuing an MSc in Applied Statistics and Data Science at Jahangirnagar University.

Work Experience:
Before diving into the world of Data Science, Amin gained practical experience through internships and jobs with two companies. This diverse experience laid the foundation for his career in data science and AI-related work.

Education:

MSc in Applied Statistics and Data Science, Jahangirnagar University (August 2022 - present)
BSc in Computer Science and Engineering, North South University (January 2016 - April 2020)
Higher Secondary School Certificate, BAF Shaheen College (2012 - 2014)
Secondary School Certificate, Sohagpur SK Pilot Model High School (2010 - 2012)
Publications:
On January 1st, 2021, Amin co-authored a publication titled "Development of Web-Based Online Medicine Delivery System for COVID-19 Pandemic." In this project, he played a key role in developing a dynamic web application for online medicine delivery during the COVID-19 pandemic.

Projects:
Amin's project portfolio is a testament to his skills and dedication. Notably, he worked on projects like the "Assessment of Academic Performances of WM-ASDS students" and the "Demographic and Health Survey Dashboard," where he used Python libraries to analyze and visualize data.

In addition, he ventured into graph representation learning and built an augmented reality mobile app for image recognition during his academic journey.

Skills:
Amin is proficient in various programming languages, including Python, R, PHP, and C++. He's also well-versed in front-end development and version control tools. His expertise extends to programming libraries such as NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, TensorFlow, Django, dplyr, and tidyr.

Interests:
Beyond his professional endeavors, Amin's interests include research, problem-solving, coding, traveling, playing football, and watching movies.

Certificates:
Amin has a "Multiple Variate Analysis" certificate, demonstrating his commitment to continuous learning and skill development.

Extra Curriculum Activities:
In his spare time, Amin discovered a passion for photography and cinematography, eventually turning it into a part-time job. This experience improved his communication skills, leadership abilities, and project management expertise.

References:

Dr. Mohammad Ashrafuzzaman Khan, Assistant Professor at North South University

Email: mohammad.khan02@northsouth.edu
Phone: +88 02 55668200 Ext – 6184
Prof. Dr. Mohammad Alamgir Kabir, Professor and Department Head at Jahangirnagar University

Email: alamgir@juniv.edu
Phone: 88027791045-51 Ext. 1798
"""

st.text_area("Your Resume/Bio:", value=resume_content, height=200)


user_input = st.text_input("Ask a question or request information:")

if user_input:
    doc = nlp(user_input)
    # Process the user's query using spaCy
    for ent in doc.ents:
        if ent.label_ == "DATE":
            st.write("Date:", ent.text)
        elif ent.label_ == "ORG":
            st.write("Organization:", ent.text)
        # Add more conditions for other entity types as needed

    # If no entities are found in the query, provide a general response
    if not doc.ents:
        st.write("I couldn't understand your request.")

import streamlit as st

# GitHub HTML link
github_html_link = "https://flappy-bird-three-plum.vercel.app/"

# Embed HTML content
st.components.v1.html("<iframe src='{}' width='500' height='700' style='border:none;'></iframe>".format(github_html_link), width=700, height=500)

import streamlit as st

# GitHub HTML link
github_html_link = "https://love-fun.vercel.app/"

# Embed HTML content
st.components.v1.html("<iframe src='{}' width='700' height='500' style='border:none;'></iframe>".format(github_html_link), width=700, height=500)

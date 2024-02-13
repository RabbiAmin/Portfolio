import streamlit as st
import requests


st.header("GitHub User Profile")


github_user = "rabbiamin"


st.markdown(f"[View {github_user}'s GitHub profile summary](https://profile-summary-for-github.com/user/{github_user})")

# Optionally, fetch and display GitHub user details via GitHub API (simplified example)
# Note: For extensive use, you'll need to authenticate with a GitHub API token

# Example: Fetch user details
url = f"https://api.github.com/users/{github_user}"
response = requests.get(url)
if response.status_code == 200:
    user_details = response.json()

    # Display some basic details
    st.write("GitHub User Details:")
    st.write(f"Name: {user_details.get('name')}")
    st.write(f"Bio: {user_details.get('bio')}")
    st.write(f"Public Repos: {user_details.get('public_repos')}")
else:
    st.error("Failed to fetch user details")

import streamlit as st
import requests

# Make API calls to your Django app
response = requests.get('https://your-django-app-url.com/pdfapp/')  # Replace with your Django app URL

# Display the response data in Streamlit
if response.status_code == 200:
    st.write(response.content)
else:
    st.write("Error occurred while fetching data from the Django app.")

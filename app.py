import streamlit as st

# Dictionary with disease names as keys and URLs as values
disease_urls = {
    "Diabetes": "https://dsproject-2-e3bqsncntsq9x7qvhidstb.streamlit.app/",
    "Heart": "https://dsproject-3-sd6c8wp3y6tqor2pgry3mh.streamlit.app/"
}

# Title for the app
st.title("Disease Prediction Portal")

# Display buttons for each disease
for disease, url in disease_urls.items():
    if st.button(disease):
        st.write(f"Redirecting to {disease} information...")
        st.markdown(f"[Click here to view details]({url})", unsafe_allow_html=True)

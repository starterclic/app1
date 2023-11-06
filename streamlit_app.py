
import streamlit as st

# Import your application modules here
from autogen_outreach.main import run as run_autogen_outreach
from rag_chatbot_confluence.src.app import run as run_rag_chatbot

PAGES = {
    "Autogen Outreach": run_autogen_outreach,
    "RAG Chatbot with Confluence": run_rag_chatbot
}

def main():
    st.sidebar.title('Application Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    # Call the app function based on the user's selection
    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()

import streamlit as st
import master_theme

def main():
    st.set_page_config(page_title="Your Web App")
    
    # Check the user's authentication status
    authenticated = True  # Set this to True if the user is authenticated

    master_theme.set_master_theme()
    master_theme.show_navbar(authenticated)

if __name__ == "__main__":
    main()

import streamlit as st
from pages import login, registration, admin, user, public

def set_master_theme():
    # Display the custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)
    
    # Create the navbar
    st.markdown("""
    <div class="navbar">
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#services">Services</a>
    <a href="#contact">Contact</a>
    </div>
    """, unsafe_allow_html=True)

def show_navbar(authenticated):
    menu = ["Home", "Login", "Registration", "Admin", "User", "Public"]
    selected_page = st.selectbox("Select a page", menu)

    # Main content
    st.title("Your Web App")

    if selected_page == "Login":
        login.show()
    elif selected_page == "Registration":
        registration.show()
    elif selected_page == "Admin":
        admin.show()
    elif selected_page == "User":
        user.show()
    elif selected_page == "Public":
        public.show()

def main():
    st.set_page_config(page_title="Your Web App")
    
    # Check the user's authentication status
    authenticated = True  # Set this to True if the user is authenticated

    master_theme.set_master_theme()
    master_theme.show_navbar(authenticated)

if __name__ == "__main__":
    main()

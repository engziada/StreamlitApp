# master_theme.py
import streamlit as st
from pages import login, registration, admin, user, public


custom_css = """
<style>
.navbar {
    background-color: #333;
    overflow: hidden;
}

.navbar a {
    float: left;
    font-size: 16px;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

.navbar a:hover {
    background-color: #ddd;
    color: black;
}
</style>
"""

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
    # st.sidebar.title("Navigation")
    
    # if authenticated:
    #     page = st.sidebar.radio("Select a page", ["Admin", "User"])
    # else:
    #     page = st.sidebar.radio("Select a page", ["Login", "Registration", "Public"])

    # if page == "Login":
    #     login.show()
    # elif page == "Registration":
    #     registration.show()
    # elif page == "Admin":
    #     admin.show()
    # elif page == "User":
    #     user.show()
    # elif page == "Public":
    #     public.show()
    # Custom menu bar
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

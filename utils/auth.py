import streamlit as st
from utils.register import register_user
from utils.login import login_user


def Auth_log_reg():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = "Guess"
        st.session_state.role = ""

    if not st.session_state.logged_in:
        menu = st.selectbox("MENU", ["LOGIN", "REGISTER"])

        if menu == "LOGIN":
            st.subheader("LOGIN")
            username = st.text_input("USERNAME")
            password = st.text_input("PASSWORD", type="password")

            log = st.button("LOGIN")
            if log:
                user = login_user(username, password)

                if user:
                    st.session_state.logged_in = True
                    st.session_state.username = user[1]
                    st.session_state.role = user[3]
                    st.rerun()
                else:
                    st.error("Invalid username or password")
    
        if menu == "REGISTER":
            st.subheader("REGISTER")
        
            username = st.text_input("USERNAME")
            password = st.text_input("PASSWORD", type="password")
            role = st.selectbox("ROLE", ["USER", "SELLER", "ADMIN"])

            if st.button("REGISTER"):
                if register_user(username, password, role):
                    st.success("Account Created Successfully")
                else:
                    st.error("Username Already Exist")
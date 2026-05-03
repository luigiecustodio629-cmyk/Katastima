import streamlit as st

User_page = st.Page(
    page= "views/users.py",
    title= "USER",
    icon= ":material/account_circle:"
)

Product_page = st.Page(
    page= "views/product.py",
    title= "PRODUCT",
    icon= ":material/shopping_bag:"
)

Cart_page = st.Page(
    page= "views/cart.py",
    title= "ADD TO CART",
    icon= ":material/add_shopping_cart:"
)

pg = st.navigation(
    {
        "Info": [User_page],
        "Dashboard": [Product_page, Cart_page]
    }
)

pg.run()

st.set_page_config(layout="wide")

st.sidebar.success(f"Logged in as {st.session_state.username}")
if st.sidebar.button("LOGOUT"):
    st.session_state.logged_in = False
    st.session_state.username = "Guess"
    st.session_state.role = ""

st.sidebar.text("MADE BY GROUP 8")
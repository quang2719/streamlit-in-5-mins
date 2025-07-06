import streamlit as st

USERS = ['admin','manager']
@st.cache_data
def fact(n):
    if n== 0: return 1
    return n*fact(n-1)

def login():
    st.title('Login page')
    username = st.text_input('User name: ')
    if st.button('Login'):
        st.session_state.user_name = username
        if username in USERS:
            st.session_state.logged_in = True
        else:
            st.session_state.logged_in = False
            st.write(f'user {st.session_state.user_name} dont have permission')
    else:
        st.warning('please enter your username')
def init():
    st.session_state.logged_in = False
    st.session_state.user_name = ""

def factorial_page():
    st.title('Factorial Calculator')
    st.write(f'hi {st.session_state.user_name}')

    num = st.number_input(
        'Enter a number between 0 and 50',
        min_value = 0,
        max_value = 50
        )
    button = st.button('Calculate')
    if button:
        res = fact(num)
        st.write(f'The factorial of {num} is {res}')

    # center alignment
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button('Log out'):
            init()

def main():
    # session state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if 'user_name' not in st.session_state:
        st.session_state.user_name = ""

    if st.session_state.logged_in:
        factorial_page()
    else:
        login()

if __name__ == '__main__':
    main()

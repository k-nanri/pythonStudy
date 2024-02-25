import streamlit as st


with st.form("my_form"):
    st.title("Let's try!!!")
    gender = st.radio("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=0, max_value=100, format="%d")
    frequency_show = st.radio('映画はよく見ますか？', ["月5回以上", "月1回", "半年に1回", "見ない"])
    good_movie = st.slider("今回の映画の評価を教えてください(0-5)", 0, 5, 0)

    submitted = st.form_submit_button("送信")
    if submitted:
        st.write("age", age, "good_movie", good_movie)



import streamlit as st
name = st. text_input("Enter Your Name : ")
fname = st. text_input("Enter the Father Nmae: ")
adr = st. text_area("Enter Your Text: ")
classdata = st.selectbox("Enter Your Class :",(1,2,3,4,5,6,7,8,9,11,12))

button = st.button("Done")
if button :
    st.markdown(f"""
    Father Name : {fname}
    address : {adr}

    class : {classdata}""")
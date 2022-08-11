import streamlit as st 

y = st.text_input("Your Name",placeholder='Enter Your Name')

x=st.selectbox('Choose an actor',['Hrithik','Akshay'])

if x == 'Hrithik':
    st.title('Hrithik Roshan')
    st.image('https://www.bollywoodhungama.com/wp-content/uploads/2021/02/WhatsApp-Image-2021-02-22-at-9.12.41-PM.jpeg', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    if st.checkbox('Wanna Rate me?',False):
        x = st.slider("Rate Me",0,9)
        st.write('So You Think I am a',x)
        if st.checkbox('Submit',False):
            st.write(str(y)+" "+'khud ko dekha hai, meko rate krega 🤭')

            st.write('Made by Jyotiradiya')


if x == 'Akshay':


    st.title('Akshay Kumar')
    st.image('https://static.toiimg.com/photo/msid-93392125/93392125.jpg?28126', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    if st.checkbox('Wanna Rate me?',False):
        x = st.slider("Rate Me",0,9)
        st.write('So You Think I am a',x)
        if st.checkbox('Submit',False):
    

            st.write(str(y)+" "+'khud ko dekha hai, meko rate krega 🤭')

            st.write('Made by Jyotiradiya')
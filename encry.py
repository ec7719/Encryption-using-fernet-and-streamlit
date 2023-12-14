from cryptography.fernet import Fernet
import streamlit as st
from pymongo import MongoClient
message = st.text_input("")
if message:
    key = Fernet.generate_key()
    fernet=Fernet(key)
    enc= fernet.encrypt(message.encode())
    enc=str(enc).strip('b')
    st.write("original string: ", message)
    st.download_button(label='Download',data=enc)
decrypt=st.button("decrypt")
if decrypt:     
    decMessage = fernet.decrypt(enc).decode()

    st.write("decrypted string: ", decMessage)

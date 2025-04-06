import streamlit as st
import random 
import string

import pyperclip
def generate_password(length,use_digits,use_special_chars):
     characters = string.ascii_letters

     if use_digits:
          characters += string.digits

     if use_special_chars:
          characters += string.punctuation
          password = ''.join(random.choice(characters) for _ in range(length))
          return password
     
st.title('Password Generator 🛡️🔐')
length = st.slider("Select password length", min_value=6, max_value=32,value=12)

use_digits = st.checkbox("Include Digits")
use_special_chars = st.checkbox("Include Special characters")

if st.button("Generate Password 🛡️🔐"):
     protected = generate_password(length,use_digits,use_special_chars)
     st.write(f"Your password is: `{protected}`")
     st.write("You can copy the password and use it in the login form")

     if protected:
          st.write("Password copied to clipboard")
          pyperclip.copy(protected)

          st.write("Built  by [Wahaj Ali](https://github.com/wahaj67)")

     
import streamlit as st

from helper import encode_message
from helper import decode_message
from constants import morse_code_dict
from constants import reverse_morse_code_dict
from constants import reverse_nato_phonetic_dict
from constants import nato_phonetic_dict


options = ('Morse code to text', 'Text to morse code', 'NATO Phonetic to text', 'Text to NATO Phonetic')


if __name__ == '__main__':
    option = st.selectbox(
        'Which telecom conversion do you want to do?',
        options
    )

    user_input = st.text_input("Enter a message:", value="... --- ...")
    
    if option == options[0]:
        morse_code_to_text = decode_message(reverse_morse_code_dict, user_input)
        st.header(morse_code_to_text)
    elif option == options[1]:
        text_to_morse_code = encode_message(morse_code_dict, user_input)
        st.header(text_to_morse_code)
    elif option == options[2]:
        nato_phonetic_to_text = decode_message(reverse_nato_phonetic_dict, user_input)
        st.header(nato_phonetic_to_text)
    elif option == options[3]:
        text_to_nato_phonetic = encode_message(nato_phonetic_dict, user_input)
        st.header(text_to_nato_phonetic)


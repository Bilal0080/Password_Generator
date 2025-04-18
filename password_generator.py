import streamlit as st
import random
import string

st.set_page_config(page_title="🔐 Unique Password & Key Generator", page_icon="🛡️", layout="centered")

st.title("🛡️ Unique Password & Key Generator")

st.markdown("## 🔐 Password Generator")
st.write("🌟 Customize your password with options below:")

# Password Settings
length = st.slider("Password Length", min_value=6, max_value=50, value=12)
use_uppercase = st.checkbox("Include Uppercase Letters", value=True)
use_lowercase = st.checkbox("Include Lowercase Letters", value=True)
use_digits = st.checkbox("Include Digits", value=True)
use_symbols = st.checkbox("Include Symbols", value=True)

def generate_password(length, upper, lower, digits, symbols):
    characters = ''
    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        return "❌ Please select at least one character set."

    return ''.join(random.choice(characters) for _ in range(length))

def get_strength(length):
    if length < 8:
        return "Weak 🔴"
    elif length < 12:
        return "Moderate 🟠"
    elif length < 20:
        return "Strong 🟡"
    else:
        return "Very Strong 🟢"

if st.button("🔒 Generate Password"):
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
    st.success("✅ Your Secure Password:")
    st.code(password, language='text')
    st.info(f"🔍 Strength: {get_strength(length)}")

    # Copy to clipboard
    st.markdown(f"""
        <button onclick=\"navigator.clipboard.writeText('{password}')\" style=\"background-color:#4CAF50; color:white; padding:10px 20px; border:none; border-radius:5px; margin-top:10px;\">
            📋 Copy Password
        </button>
        """, unsafe_allow_html=True)

# License Key Generator Section
st.markdown("---")
st.markdown("## 🔑 License Key Generator")
st.write("💡 Generate API-style or license-style keys (e.g., XXXX-XXXX-XXXX)")

sections = st.number_input("Number of Sections", min_value=2, max_value=10, value=4)
chars_per_section = st.number_input("Characters per Section", min_value=2, max_value=10, value=4)

def generate_key(sections, chars_per_section):
    charset = string.ascii_uppercase + string.digits
    return '-'.join(''.join(random.choice(charset) for _ in range(chars_per_section)) for _ in range(sections))

if st.button("🔑 Generate License Key"):
    key = generate_key(sections, chars_per_section)
    st.success("✅ Your License Key:")
    st.code(key, language='text')

    # Copy to clipboard
    st.markdown(f"""
        <button onclick=\"navigator.clipboard.writeText('{key}')\" style=\"background-color:#0073e6; color:white; padding:10px 20px; border:none; border-radius:5px; margin-top:10px;\">
            📋 Copy Key
        </button>
        """, unsafe_allow_html=True)

import streamlit as st
from app.components.mpbf_display import display_mpbf
from app.components.dp_display import display_dp
from app.components.compliance_display import display_compliance_ai
from backend.model_loader import load_model
import os

# Load model on startup
@st.cache_resource
def load_model_on_start():
    model_path = "models/model3_gpt2"  # Adjust path if necessary
    model, tokenizer = load_model(model_path)
    return model, tokenizer

# Load the model when the app starts
model, tokenizer = load_model_on_start()

# Load custom CSS
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"⚠️ CSS file '{file_name}' not found.")

# Apply style
local_css("app/style.css")

# Custom CSS to center the title
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #4CAF50;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown('<div class="title">Working Capital Management</div>', unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("AADISWAN Tools")
selected_section = st.sidebar.radio("Select Section", ["MPBF", "Drawing Power", "RBI Compliance AI"])

# Initialize session state
if "years" not in st.session_state:
    st.session_state.years = ["Year 1"]

# Routing
if selected_section == "MPBF":
    display_mpbf()
elif selected_section == "Drawing Power":
    display_dp()
elif selected_section == "RBI Compliance AI":
    display_compliance_ai(model, tokenizer)

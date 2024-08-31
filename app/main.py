# app/main.py

import streamlit as st
from app.supervisor import Supervisor
from app.logging_config import setup_logging

# Setup logging
setup_logging()

# Initialize Supervisor
supervisor = Supervisor()

# Streamlit UI
st.title("Student Management System - LLM Agent")

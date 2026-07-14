

from __future__ import annotations

import streamlit as st


def initialize_state() -> None:
    """
    Initializes all application session state
    variables.

    This ensures state persistence across reruns
    and prepares the project for future LLM
    integration.
    """

    defaults = {

       
        # Data
       

        "df": None,

        "filtered_df": None,

       
        # Navigation
       

        "current_page": "Dashboard",

       
        # Global Filters
       

        "selected_year": "All",

        "selected_city": "All",

       
        # Page Specific Filters
       

        "selected_startup": None,

        "selected_investor": None,

       
        # Future AI
       

        "llm_enabled": False,

        "chat_history": [],

        "vector_store": None

    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value
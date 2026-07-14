from __future__ import annotations

import streamlit as st


def get_navigation() -> str:
    """
    Returns selected page.
    """

    pages = [
        "Dashboard",
        "Startup Analysis",
        "Investor Analysis"
    ]

    page = st.sidebar.radio(
        "Navigation",
        pages
    )

    st.session_state.current_page = page

    return page
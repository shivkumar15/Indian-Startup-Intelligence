from __future__ import annotations

import streamlit as st

from .navigation import get_navigation
from .filters import (
    apply_filters,
    startup_options,
    investor_options,
)


def build_sidebar(df):
    """
    Builds the application sidebar.
    """

    st.sidebar.title("Indian Startup Intelligence")

    page = get_navigation()

    st.sidebar.divider()

    filtered_df = apply_filters(df)

    selected_startup = None
    selected_investor = None

    if page == "Startup Analysis":

        startups = startup_options(filtered_df)

        if startups:

            selected_startup = st.sidebar.selectbox(
                "Startup",
                startups,
                key="selected_startup"
            )

        else:

            st.sidebar.warning(
                "No startups found."
            )

    elif page == "Investor Analysis":

        investors = investor_options(filtered_df)

        if investors:

            selected_investor = st.sidebar.selectbox(
                "Investor",
                investors,
                key="selected_investor"
            )

        else:

            st.sidebar.warning(
                "No investors found."
            )

    return {
        "page": page,
        "filtered_df": filtered_df,
        "selected_year": st.session_state.selected_year,
        "selected_city": st.session_state.selected_city,
        "selected_startup": selected_startup,
        "selected_investor": selected_investor,
    }
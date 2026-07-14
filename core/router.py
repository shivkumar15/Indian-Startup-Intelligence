from __future__ import annotations

import streamlit as st

from pages.overall import show_overall_dashboard
from pages.startup import show_startup_dashboard
from pages.investor import show_investor_dashboard


def route_page(
    page: str,
    filtered_df,
    selected_year: str,
    selected_city: str,
    selected_startup: str | None,
    selected_investor: str | None,
) -> None:
    """
    Routes the user to the selected page.
    """

    if page == "Dashboard":

        show_overall_dashboard(
            df=filtered_df,
            selected_year=selected_year,
            selected_city=selected_city,
        )

    elif page == "Startup Analysis":

        if selected_startup is None:

            st.info(
                "Please select a startup from the sidebar."
            )

            return

        show_startup_dashboard(
            df=filtered_df,
            selected_startup=selected_startup,
        )

    elif page == "Investor Analysis":

        if selected_investor is None:

            st.info(
                "Please select an investor from the sidebar."
            )

            return

        show_investor_dashboard(
            df=filtered_df,
            selected_investor=selected_investor,
        )

    else:

        st.error("Unknown page selected.")
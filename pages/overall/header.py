

from __future__ import annotations

import streamlit as st

from config import (
    APP_NAME,
    APP_SUBTITLE,
    APP_VERSION,
    AUTHOR,
)


class DashboardHeader:
    """
    Renders the dashboard header.
    """

    @staticmethod
    def render(
        summary: dict,
        selected_year: str = "All",
        selected_city: str = "All",
    ) -> None:

        
        # Title
        

        st.title(APP_NAME)

        st.caption(APP_SUBTITLE)

        st.markdown("---")

        
        # Dataset Information
        

        col1, col2, col3 = st.columns(3)

        with col1:

            st.info(
                f"""
**Dataset Records**

{summary["rows"]:,}
"""
            )

        with col2:

            st.info(
                f"""
**Columns**

{summary["columns"]}
"""
            )

        with col3:

            st.info(
                f"""
**Missing Values**

{summary["missing_values"]:,}
"""
            )

        st.markdown("")

        
        # Active Filters
        

        left, right = st.columns(2)

        with left:

            st.caption(
                f"**Year Filter:** {selected_year}"
            )

        with right:

            st.caption(
                f"**City Filter:** {selected_city}"
            )

        st.markdown("---")

        
        # Footer Information
        

        st.caption(
            f"""
Version **{APP_VERSION}** • Developed by **{AUTHOR}**
"""
        )
"""
=========================================================
Indian Startup Intelligence
Startup Funding History

Author  : Shiv Kumar
Version : 2.0
=========================================================
"""

from __future__ import annotations

import streamlit as st

from utils.analytics import StartupAnalytics


class StartupHistory:
    """
    Displays startup funding history
    and download option.
    """

    @staticmethod
    def render(
        df,
        startup: str
    ) -> None:

        st.subheader("Funding History")

        history = StartupAnalytics.get_history(
            df,
            startup
        )

        if history.empty:

            st.info(
                "No funding history available."
            )

            return

       
        # Funding History Table
       

        st.dataframe(

            history,

            hide_index=True,

            use_container_width=True

        )

        st.caption(
            """
Amount = 0 indicates that the funding amount
was not publicly disclosed.
"""
        )

        st.markdown("")

       
        # Recent Funding
       

        st.subheader("Recent Funding Rounds")

        recent = StartupAnalytics.get_recent_funding(

            df,

            startup,

            limit=5

        )

        st.dataframe(

            recent,

            hide_index=True,

            use_container_width=True

        )

        st.markdown("")

       
        # Download Report
       

        st.download_button(

            label="Download Startup Report",

            data=history.to_csv(index=False),

            file_name=f"{startup}_report.csv",

            mime="text/csv",

            use_container_width=True

        )
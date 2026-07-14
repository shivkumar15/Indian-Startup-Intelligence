
from __future__ import annotations

import streamlit as st

from utils.analytics import StartupAnalytics


class StartupSummary:
    """
    Renders startup summary information.
    """

    @staticmethod
    def render(df, startup: str) -> None:

        summary = StartupAnalytics.get_summary(
            df,
            startup
        )

        if not summary:

            st.warning(
                "No startup information available."
            )
            return

        # =================================================
        # Startup Name
        # =================================================

        st.title(summary["startup"])

        st.caption(
            "Complete funding profile of the selected startup."
        )

        st.markdown("---")

        # =================================================
        # Basic Information
        # =================================================

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "City",
                summary["city"]
            )

        with col2:

            st.metric(
                "Sector",
                summary["vertical"]
            )

        with col3:

            st.metric(
                "Sub Sector",
                summary["subvertical"]
            )

        st.markdown("")

        # =================================================
        # KPI Cards
        # =================================================

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Total Funding",
                f"₹ {summary['total_funding']:,} Cr"
            )

        with col2:

            st.metric(
                "Funding Rounds",
                summary["funding_rounds"]
            )

        with col3:

            st.metric(
                "Unique Investors",
                summary["total_investors"]
            )

        with col4:

            st.metric(
                "Average Round",
                f"₹ {summary['average_round']:,} Cr"
            )

        st.markdown("---")
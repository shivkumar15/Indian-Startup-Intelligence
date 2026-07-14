

from __future__ import annotations

import streamlit as st


class DashboardMetrics:
    """
    Renders KPI cards for the dashboard.
    """

    @staticmethod
    def render(summary: dict) -> None:

        if not summary:

            st.warning("No summary data available.")
            return

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                label="Total Funding",
                value=f"₹ {summary['total_funding']:,} Cr"
            )

        with col2:

            st.metric(
                label="Funded Startups",
                value=f"{summary['total_startups']:,}"
            )

        with col3:

            st.metric(
                label="Unique Investors",
                value=f"{summary['total_investors']:,}"
            )

        with col4:

            st.metric(
                label="Average Funding",
                value=f"₹ {summary['average_funding']:,} Cr"
            )

        st.markdown("---")
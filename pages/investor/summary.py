

from __future__ import annotations

import streamlit as st

from utils.analytics import InvestorAnalytics


class InvestorSummary:
    """
    Renders investor summary information.
    """

    @staticmethod
    def render(
        df,
        investor: str
    ) -> None:

        summary = InvestorAnalytics.get_summary(
            df,
            investor
        )

        if not summary:

            st.warning(
                "No investor information available."
            )

            return

       
        # Header
       

        st.title(summary["investor"])

        st.caption(
            "Complete investment profile of the selected investor."
        )

        st.markdown("---")

       
        # KPI Cards
       

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Total Investment",
                f"₹ {summary['total_investment']:,} Cr"
            )

        with col2:

            st.metric(
                "Funded Startups",
                summary["total_startups"]
            )

        with col3:

            st.metric(
                "Favourite Sector",
                summary["favorite_sector"]
            )

        with col4:

            st.metric(
                "Favourite City",
                summary["favorite_city"]
            )

        st.markdown("")

       
        # Secondary KPI Cards
       

        average = InvestorAnalytics.get_average_investment(
            df,
            investor
        )

        col5, col6 = st.columns(2)

        with col5:

            st.metric(
                "Investment Rounds",
                summary["investment_rounds"]
            )

        with col6:

            st.metric(
                "Average Investment",
                f"₹ {average:,.2f} Cr"
            )

        st.markdown("---")
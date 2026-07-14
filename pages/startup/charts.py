"""
=========================================================
Indian Startup Intelligence
Startup Charts

Author  : Shiv Kumar
Version : 2.0
=========================================================
"""

from __future__ import annotations

import streamlit as st

from utils.analytics import StartupAnalytics
from utils.charts import ChartFactory


class StartupCharts:
    """
    Renders all startup charts.
    """

    @staticmethod
    def render(
        df,
        startup: str
    ) -> None:

        if df.empty:

            st.warning(
                "No startup data available."
            )

            return

        
        # Funding Timeline
        

        st.subheader("Funding Timeline")

        timeline = StartupAnalytics.get_timeline(
            df,
            startup
        )

        fig = ChartFactory.line_chart(

            dataframe=timeline,

            x="date",

            y="amount",

            title="Funding Timeline"

        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown("---")

        
        # Round Distribution
        

        col1, col2 = st.columns(2)

        with col1:

            round_df = (
                StartupAnalytics
                .get_round_distribution(
                    df,
                    startup
                )
            )

            fig = ChartFactory.donut_chart(

                dataframe=round_df,

                names="round",

                values="amount",

                title="Funding by Round"

            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        
        # Investor Distribution
        

        with col2:

            investor_df = (
                StartupAnalytics
                .get_investor_distribution(
                    df,
                    startup
                )
            )

            fig = ChartFactory.horizontal_bar(

                dataframe=investor_df,

                x="count",

                y="investor",

                title="Top Investors"

            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.markdown("---")

        
        # Yearly Funding
        

        yearly = (
            StartupAnalytics
            .get_yearly_funding(
                df,
                startup
            )
        )

        fig = ChartFactory.bar(

            dataframe=yearly,

            x="year",

            y="amount",

            title="Year-wise Funding"

        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
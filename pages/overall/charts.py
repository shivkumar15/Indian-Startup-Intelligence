

from __future__ import annotations

import streamlit as st

from utils.analytics import DashboardAnalytics
from utils.charts import ChartFactory


class DashboardCharts:
    """
    Renders all dashboard charts.
    """

    @staticmethod
    def render(df):

        if df.empty:
            st.warning("No data available for selected filters.")
            return

        # Monthly Funding Trend

        st.subheader("Funding Trend")

        trend = DashboardAnalytics.get_monthly_trend(df)

        fig = ChartFactory.line_chart(
            dataframe=trend,
            x="label",
            y="amount",
            title="Monthly Funding Trend"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown("---")

        # Top Startups & Investors

        col1, col2 = st.columns(2)

        with col1:

            startup = DashboardAnalytics.get_top_startups(df)

            fig = ChartFactory.horizontal_bar(
                dataframe=startup,
                x="amount",
                y="startup",
                title="Top Funded Startups"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with col2:

            investor = DashboardAnalytics.get_top_investors(df)

            fig = ChartFactory.horizontal_bar(
                dataframe=investor,
                x="amount",
                y="investors",
                title="Top Investors"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.markdown("---")

        # City & Sector

        col3, col4 = st.columns(2)

        with col3:

            city = DashboardAnalytics.get_top_cities(df)

            fig = ChartFactory.horizontal_bar(
                dataframe=city,
                x="amount",
                y="city",
                title="Top Funding Cities"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with col4:

            sector = DashboardAnalytics.get_top_sectors(df)

            fig = ChartFactory.horizontal_bar(
                dataframe=sector,
                x="amount",
                y="vertical",
                title="Top Funding Sectors"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.markdown("---")

        # Funding Round Distribution

        st.subheader("Funding Round Distribution")

        rounds = DashboardAnalytics.get_round_distribution(df)

        fig = ChartFactory.donut_chart(
            dataframe=rounds,
            names="round",
            values="amount",
            title="Funding by Round"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown("---")

        # Download Data

        st.download_button(
            label="Download Current Dataset",
            data=df.to_csv(index=False),
            file_name="startup_filtered_data.csv",
            mime="text/csv",
            use_container_width=True
        )
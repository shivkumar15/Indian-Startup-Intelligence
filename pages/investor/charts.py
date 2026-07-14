

from __future__ import annotations

import streamlit as st

from utils.analytics import InvestorAnalytics
from utils.charts import ChartFactory


class InvestorCharts:
    """
    Renders all investor related charts.
    """

    @staticmethod
    def render(
        df,
        investor: str
    ) -> None:

        if df.empty:

            st.warning(
                "No investor data available."
            )

            return

        
        # Investment Timeline
        

        st.subheader("Investment Timeline")

        timeline = InvestorAnalytics.get_timeline(
            df,
            investor
        )

        fig = ChartFactory.line_chart(

            dataframe=timeline,

            x="year",

            y="amount",

            title="Year-wise Investment"

        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown("---")

        
        # Startup Portfolio & Funding Round
        

        col1, col2 = st.columns(2)

        with col1:

            portfolio = InvestorAnalytics.get_portfolio(
                df,
                investor
            )

            fig = ChartFactory.horizontal_bar(

                dataframe=portfolio,

                x="amount",

                y="startup",

                title="Startup Portfolio"

            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with col2:

            rounds = InvestorAnalytics.get_round_distribution(
                df,
                investor
            )

            fig = ChartFactory.donut_chart(

                dataframe=rounds,

                names="round",

                values="amount",

                title="Funding Round Distribution"

            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.markdown("---")

        
        # Sector & City Distribution
        

        col3, col4 = st.columns(2)

        with col3:

            sector = InvestorAnalytics.get_sector_distribution(
                df,
                investor
            )

            fig = ChartFactory.horizontal_bar(

                dataframe=sector,

                x="amount",

                y="vertical",

                title="Sector Distribution"

            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with col4:

            city = InvestorAnalytics.get_city_distribution(
                df,
                investor
            )

            fig = ChartFactory.horizontal_bar(

                dataframe=city,

                x="amount",

                y="city",

                title="City Distribution"

            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.markdown("---")

        
        # Largest Investments
        

        st.subheader("Largest Investments")

        largest = InvestorAnalytics.get_largest_investments(
            df,
            investor
        )

        fig = ChartFactory.horizontal_bar(

            dataframe=largest,

            x="amount",

            y="startup",

            title="Top Investments"

        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
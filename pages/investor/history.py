

from __future__ import annotations

import streamlit as st

from utils.analytics import InvestorAnalytics


class InvestorHistory:
    """
    Displays recent investments and
    download report section.
    """

    @staticmethod
    def render(
        df,
        investor: str
    ) -> None:

        st.subheader("Recent Investments")

        recent = InvestorAnalytics.get_recent_investments(
            df,
            investor
        )

        if recent.empty:

            st.info(
                "No investments found."
            )

            return

        
        # Recent Investments Table
        

        st.dataframe(

            recent,

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

        
        # Quick Statistics
        

        col1, col2 = st.columns(2)

        with col1:

            st.metric(

                "Displayed Investments",

                len(recent)

            )

        with col2:

            st.metric(

                "Displayed Funding",

                f"₹ {round(recent['amount'].sum()):,} Cr"

            )

        st.markdown("")

        
        # Download Report
        

        st.download_button(

            label="Download Investor Report",

            data=recent.to_csv(index=False),

            file_name=f"{investor}_report.csv",

            mime="text/csv",

            use_container_width=True

        )

        st.markdown("---")

        st.caption(
            """
This report contains the latest investment
records for the selected investor.
"""
        )
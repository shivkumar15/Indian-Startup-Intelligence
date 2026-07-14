

from __future__ import annotations

import streamlit as st

from utils.analytics import Insights


class DashboardInsights:
    """
    Renders dashboard insights.

    Currently uses rule-based insights.

    Future:
        Replace with LLM generated insights
        without changing the UI.
    """

    @staticmethod
    def render(df) -> None:

        st.subheader("Dashboard Insights")

        insights = Insights.dashboard(df)

        if not insights:

            st.info("No insights available.")

            return

        for insight in insights:

            st.info(

                f"""
### {insight["title"]}

{insight["description"]}
"""

            )

        st.markdown("---")

        st.caption(
            """
These insights are generated using the analytics engine.

Future versions will support AI-generated business insights
using OpenAI / Gemini / Claude.
"""
        )


from __future__ import annotations

import streamlit as st

from utils.analytics import DashboardAnalytics

from .header import DashboardHeader
from .metrics import DashboardMetrics
from .charts import DashboardCharts
from .insights import DashboardInsights


def show_overall_dashboard(
    df,
    selected_year: str = "All",
    selected_city: str = "All"
):
    """
    Render the complete Overall Dashboard.
    """

    
    # Empty Dataset
    

    if df.empty:

        st.warning(
            """
No data available for the selected filters.

Try changing the Year or City filter.
"""
        )

        return

    
    # Summary
    

    summary = DashboardAnalytics.get_summary(df)

    
    # Header
    

    DashboardHeader.render(
        summary=summary,
        selected_year=selected_year,
        selected_city=selected_city
    )

    
    # KPI Cards
    

    DashboardMetrics.render(summary)

    
    # Charts
    

    DashboardCharts.render(df)

    
    # Insights
    

    DashboardInsights.render(df)

    
    # Footer
    

    st.markdown("---")

    st.caption(
        """
Data Source : Indian Startup Funding Dataset

Amount = 0 means the funding amount was not publicly disclosed.

Dashboard Version : 2.0
"""
    )
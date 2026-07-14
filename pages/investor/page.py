

from __future__ import annotations

import streamlit as st

from .summary import InvestorSummary
from .charts import InvestorCharts
from .history import InvestorHistory


def show_investor_dashboard(
    df,
    selected_investor: str
) -> None:
    """
    Renders the complete Investor Dashboard.
    """

   
    # Empty Dataset
   

    if df.empty:

        st.warning(
            """
No investor data available for the selected filters.

Try selecting another Year or City.
"""
        )

        return

   
    # Investor Validation
   

    if not selected_investor:

        st.info(
            "Please select an investor."
        )

        return

   
    # Summary
   

    InvestorSummary.render(

        df,

        selected_investor

    )

   
    # Charts
   

    InvestorCharts.render(

        df,

        selected_investor

    )

   
    # History
   

    InvestorHistory.render(

        df,

        selected_investor

    )

   
    # Footer
   

    st.markdown("---")

    st.caption(
        """
Investor Analysis Module


"""
    )
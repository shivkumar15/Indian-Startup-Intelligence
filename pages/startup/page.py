

from __future__ import annotations

import streamlit as st

from .summary import StartupSummary
from .charts import StartupCharts
from .history import StartupHistory


def show_startup_dashboard(
    df,
    selected_startup: str
) -> None:
    """
    Renders the complete Startup Dashboard.
    """

    
    # Empty Dataset
    

    if df.empty:

        st.warning(
            """
No startup data available for the selected filters.

Try selecting another Year or City.
"""
        )

        return

    
    # Startup Selection Validation
    

    if selected_startup not in df["startup"].unique():

        st.info(
            "Please select a valid startup."
        )

        return

    
    # Summary
    

    StartupSummary.render(

        df,

        selected_startup

    )

    
    # Charts
    

    StartupCharts.render(

        df,

        selected_startup

    )

    
    # Funding History
    

    StartupHistory.render(

        df,

        selected_startup

    )
 
    # Footer
    
    st.markdown("---")

    st.caption(
        """
Startup Analysis Module


"""
    )
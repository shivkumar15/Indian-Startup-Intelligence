"""
=========================================================
Indian Startup Intelligence
Rule Based Insights

Author  : Shiv Kumar
Version : 2.0
=========================================================
"""

from __future__ import annotations

import pandas as pd


class Insights:
    """
    Generates rule-based insights.

    Later this module can be replaced
    with LLM generated insights without
    changing the UI.
    """

    # =====================================================
    # Dashboard Insights
    # =====================================================

    @staticmethod
    def dashboard(df: pd.DataFrame) -> list[dict]:

        if df.empty:

            return []

        top_city = (
            df.groupby("city")["amount"]
            .sum()
            .idxmax()
        )

        top_sector = (
            df.groupby("vertical")["amount"]
            .sum()
            .idxmax()
        )

        top_startup = (
            df.groupby("startup")["amount"]
            .sum()
            .idxmax()
        )

        top_year = (
            df.groupby("year")["amount"]
            .sum()
            .idxmax()
        )

        total = round(df["amount"].sum())

        return [

            {
                "title": "Total Funding",
                "description": f"₹ {total:,} Cr funding recorded in the selected dataset."
            },

            {
                "title": "Top City",
                "description": f"{top_city} attracted the highest investment."
            },

            {
                "title": "Top Sector",
                "description": f"{top_sector} received the maximum funding."
            },

            {
                "title": "Top Startup",
                "description": f"{top_startup} raised the highest funding."
            },

            {
                "title": "Peak Funding Year",
                "description": f"The highest funding activity was recorded in {int(top_year)}."
            }

        ]

    # =====================================================
    # Startup Insights
    # =====================================================

    @staticmethod
    def startup(
        df: pd.DataFrame,
        startup: str
    ) -> list[str]:

        startup_df = df[
            df["startup"] == startup
        ]

        if startup_df.empty:
            return [
                "No startup information available."
            ]

        insights = []

        total = round(
            startup_df["amount"].sum()
        )

        rounds = startup_df.shape[0]

        investors = set()

        for row in startup_df["investors"]:

            for investor in str(row).split(","):

                investor = investor.strip()

                if investor:
                    investors.add(investor)

        biggest_round = (
            startup_df.loc[
                startup_df["amount"].idxmax(),
                "round"
            ]
        )

        insights.append({
            "title": "Total Funding",
            "description": f"{startup} has raised ₹{total:,} Cr."
        })

        insights.append({
            "title": "Funding Rounds",
            "description": f"{rounds} funding rounds completed."
        })

        insights.append({
            "title": "Investors",
            "description": f"{len(investors)} unique investors participated."
        })

        insights.append({
            "title": "Largest Round",
            "description": f"The largest funding came during '{biggest_round}'."
        })

        return insights

    # =====================================================
    # Investor Insights
    # =====================================================

    @staticmethod
    def investor(
        df: pd.DataFrame,
        investor: str
    ) -> list[str]:

        investor_df = df[
            df["investors"].str.contains(
                investor,
                case=False,
                na=False
            )
        ]

        if investor_df.empty:
            return [
                "No investor information available."
            ]

        insights = []

        total = round(
            investor_df["amount"].sum()
        )

        startups = (
            investor_df["startup"]
            .nunique()
        )

        favorite_sector = (
            investor_df
            .groupby("vertical")["amount"]
            .sum()
            .idxmax()
        )

        favorite_city = (
            investor_df
            .groupby("city")["amount"]
            .sum()
            .idxmax()
        )

        insights.append({
            "title": "Total Investment",
            "description": f"{investor} invested ₹{total:,} Cr."
        })

        insights.append({
            "title": "Portfolio",
            "description": f"Invested in {startups} startups."
        })

        insights.append({
            "title": "Favourite Sector",
            "description": favorite_sector
        })

        insights.append({
            "title": "Favourite City",
            "description": favorite_city
        })

        return insights
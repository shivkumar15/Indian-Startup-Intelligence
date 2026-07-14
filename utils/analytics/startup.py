"""
=========================================================
Indian Startup Intelligence
Startup Analytics

Author  : Shiv Kumar
Version : 2.0
=========================================================
"""

from __future__ import annotations

import pandas as pd


class StartupAnalytics:
    """
    Performs all startup related analytics.
    """

    # =====================================================
    # Startup Summary
    # =====================================================

    @staticmethod
    def get_summary(
        df: pd.DataFrame,
        startup: str
    ) -> dict:

        startup_df = df[df["startup"] == startup]

        if startup_df.empty:
            return {}

        investors = set()

        for row in startup_df["investors"]:

            for investor in str(row).split(","):

                investor = investor.strip()

                if investor:
                    investors.add(investor)

        return {

            "startup": startup,

            "city": startup_df["city"].iloc[0],

            "vertical": startup_df["vertical"].iloc[0],

            "subvertical": startup_df["subvertical"].fillna("Undisclosed").iloc[0],

            "total_funding":
                round(startup_df["amount"].sum()),

            "funding_rounds":
                startup_df.shape[0],

            "average_round":
                round(startup_df["amount"].mean()),

            "total_investors":
                len(investors)

        }

    # =====================================================
    # Funding Timeline
    # =====================================================

    @staticmethod
    def get_timeline(
        df: pd.DataFrame,
        startup: str
    ) -> pd.DataFrame:

        startup_df = (

            df[df["startup"] == startup]

            .sort_values("date")

        )

        return startup_df[
            [
                "date",
                "amount"
            ]
        ]

    # =====================================================
    # Funding By Round
    # =====================================================

    @staticmethod
    def get_round_distribution(
        df: pd.DataFrame,
        startup: str
    ) -> pd.DataFrame:

        startup_df = df[df["startup"] == startup]

        return (

            startup_df

            .groupby("round")["amount"]

            .sum()

            .reset_index()

        )

    # =====================================================
    # Investor Distribution
    # =====================================================

    @staticmethod
    def get_investor_distribution(
        df: pd.DataFrame,
        startup: str
    ) -> pd.DataFrame:

        startup_df = df[df["startup"] == startup]

        investors = []

        for row in startup_df["investors"]:

            investors.extend(

                [

                    investor.strip()

                    for investor in str(row).split(",")

                    if investor.strip()

                ]

            )

        investor_df = (

            pd.Series(investors)

            .value_counts()

            .reset_index()

        )

        investor_df.columns = [

            "investor",

            "count"

        ]

        return investor_df

    # =====================================================
    # Funding History
    # =====================================================

    @staticmethod
    def get_history(
        df: pd.DataFrame,
        startup: str
    ) -> pd.DataFrame:

        startup_df = (

            df[df["startup"] == startup]

            .sort_values(

                "date",

                ascending=False

            )

        )

        history= startup_df[
            [

                "date",

                "round",

                "investors",

                "amount"

            ]

        ].copy()
        history["date"] = history["date"].dt.strftime("%d-%b-%Y")
        return history
    # =====================================================
    # Funding Per Round
    # =====================================================

    @staticmethod
    def get_round_wise_funding(
        df: pd.DataFrame,
        startup: str
    ) -> pd.DataFrame:

        startup_df = df[df["startup"] == startup]

        return (

            startup_df

            .groupby("round")["amount"]

            .agg(

                total_funding="sum",

                average_funding="mean",

                funding_count="count"

            )

            .reset_index()

        )

    # =====================================================
    # Yearly Funding
    # =====================================================

    @staticmethod
    def get_yearly_funding(
        df: pd.DataFrame,
        startup: str
    ) -> pd.DataFrame:

        startup_df = df[df["startup"] == startup]

        return (

            startup_df

            .groupby("year")["amount"]

            .sum()

            .reset_index()

            .sort_values("year")

        )

    # =====================================================
    # Recent Funding
    # =====================================================

    @staticmethod
    def get_recent_funding(
        df: pd.DataFrame,
        startup: str,
        limit: int = 5
    ) -> pd.DataFrame:

        startup_df = (

            df[df["startup"] == startup]

            .sort_values(

                "date",

                ascending=False

            )

        )

        recent= startup_df.head(limit)[

            [

                "date",

                "round",

                "investors",

                "amount"

            ]

        ].copy()

        recent["date"] = recent["date"].dt.strftime("%d-%b-%Y")
        return recent
"""
=========================================================
Indian Startup Intelligence
Investor Analytics

Author  : Shiv Kumar
Version : 2.0
=========================================================
"""

from __future__ import annotations

import pandas as pd


class InvestorAnalytics:
    """
    Performs all investor related analytics.
    """

    # =====================================================
    # Investor Summary
    # =====================================================

    @staticmethod
    def get_summary(
        df: pd.DataFrame,
        investor: str
    ) -> dict:

        investor_df = df[
            df["investors"].str.contains(
                investor,
                case=False,
                na=False
            )
        ]

        if investor_df.empty:
            return {}

        return {

            "investor": investor,

            "total_investment":
                round(
                    investor_df["amount"].sum()
                ),

            "total_startups":
                investor_df["startup"].nunique(),

            "favorite_sector":
                investor_df.groupby(
                    "vertical"
                )["amount"].sum().idxmax(),

            "favorite_city":
                investor_df.groupby(
                    "city"
                )["amount"].sum().idxmax(),

            "investment_rounds":
                investor_df.shape[0]

        }

    # =====================================================
    # Investment Timeline
    # =====================================================

    @staticmethod
    def get_timeline(
        df: pd.DataFrame,
        investor: str
    ) -> pd.DataFrame:

        investor_df = df[
            df["investors"].str.contains(
                investor,
                case=False,
                na=False
            )
        ]

        timeline= (

            investor_df

            .groupby("year")["amount"]

            .sum()

            .reset_index()

            .sort_values("year")

        )

        timeline['year']=timeline['year'].astype(int)
        return timeline
    # =====================================================
    # Startup Portfolio
    # =====================================================

    @staticmethod
    def get_portfolio(
        df: pd.DataFrame,
        investor: str
    ) -> pd.DataFrame:

        investor_df = df[
            df["investors"].str.contains(
                investor,
                case=False,
                na=False
            )
        ]

        return (

            investor_df

            .groupby("startup")["amount"]

            .sum()

            .sort_values(

                ascending=False

            )

            .reset_index()

        )

    # =====================================================
    # Sector Distribution
    # =====================================================

    @staticmethod
    def get_sector_distribution(
        df: pd.DataFrame,
        investor: str
    ) -> pd.DataFrame:

        investor_df = df[
            df["investors"].str.contains(
                investor,
                case=False,
                na=False
            )
        ]

        return (

            investor_df

            .groupby("vertical")["amount"]

            .sum()

            .reset_index()

        )

    # =====================================================
    # City Distribution
    # =====================================================

    @staticmethod
    def get_city_distribution(
        df: pd.DataFrame,
        investor: str
    ) -> pd.DataFrame:

        investor_df = df[
            df["investors"].str.contains(
                investor,
                case=False,
                na=False
            )
        ]

        return (

            investor_df

            .groupby("city")["amount"]

            .sum()

            .reset_index()

        )

    # =====================================================
    # Funding Round Distribution
    # =====================================================

    @staticmethod
    def get_round_distribution(
        df: pd.DataFrame,
        investor: str
    ) -> pd.DataFrame:

        investor_df = df[
            df["investors"].str.contains(
                investor,
                case=False,
                na=False
            )
        ]

        return (

            investor_df

            .groupby("round")["amount"]

            .sum()

            .reset_index()

        )

    # =====================================================
    # Recent Investments
    # =====================================================

    @staticmethod
    def get_recent_investments(
        df: pd.DataFrame,
        investor: str,
        limit: int = 10
    ) -> pd.DataFrame:

        investor_df = df[
            df["investors"].str.contains(
                investor,
                case=False,
                na=False
            )
        ]

        investor_df = investor_df.sort_values(
            "date",
            ascending=False
        )

        recent= investor_df.head(limit)[
            [
                "date",
                "startup",
                "vertical",
                "city",
                "round",
                "amount"
            ]
        ].copy()
        recent["date"] = recent["date"].dt.strftime("%d-%b-%Y")
        return recent
    # =====================================================
    # Largest Investments
    # =====================================================

    @staticmethod
    def get_largest_investments(
        df: pd.DataFrame,
        investor: str,
        limit: int = 10
    ) -> pd.DataFrame:

        investor_df = df[
            df["investors"].str.contains(
                investor,
                case=False,
                na=False
            )
        ]

        return (

            investor_df

            .groupby("startup")["amount"]

            .sum()

            .sort_values(

                ascending=False

            )

            .head(limit)

            .reset_index()

        )

    # =====================================================
    # Average Investment
    # =====================================================

    @staticmethod
    def get_average_investment(
        df: pd.DataFrame,
        investor: str
    ) -> float:

        investor_df = df[
            df["investors"].str.contains(
                investor,
                case=False,
                na=False
            )
        ]

        if investor_df.empty:
            return 0

        return round(

            investor_df["amount"].mean(),

            2

        )
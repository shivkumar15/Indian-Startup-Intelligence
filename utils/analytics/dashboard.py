"""
=========================================================
Indian Startup Intelligence
Dashboard Analytics

Author  : Shiv Kumar
Version : 2.0
=========================================================
"""

from __future__ import annotations

import pandas as pd

from config import TOP_N


class DashboardAnalytics:
    """
    Performs all dashboard related analytics.
    """

    # =====================================================
    # Dashboard Summary
    # =====================================================

    @staticmethod
    def get_summary(df: pd.DataFrame) -> dict:

        investors = set()

        for row in df["investors"]:

            for investor in str(row).split(","):

                investor = investor.strip()

                if investor:

                    investors.add(investor)

        return {

            "total_funding":
                round(df["amount"].sum()),

            "total_startups":
                df["startup"].nunique(),

            "total_investors":
                len(investors),

            "average_funding":
                round(
                    df.groupby("startup")["amount"]
                    .sum()
                    .mean()
                ),

            "rows":
                len(df),

            "columns":
                len(df.columns),

            "missing_values":
                int(df.isna().sum().sum())

        }

    # =====================================================
    # Monthly Trend
    # =====================================================

    @staticmethod
    def get_monthly_trend(
        df: pd.DataFrame
    ) -> pd.DataFrame:

        import calendar

        trend = (

            df

            .groupby(
                ["year", "month"]
            )["amount"]

            .sum()

            .reset_index()

            .sort_values(
                ["year", "month"]
            )

        )

        trend["label"] = trend.apply(

            lambda row:

            f"{calendar.month_abbr[int(row['month'])]}-{int(row['year'])}",

            axis=1

        )

        return trend

    # =====================================================
    # Yearly Trend
    # =====================================================

    @staticmethod
    def get_yearly_trend(
        df: pd.DataFrame
    ) -> pd.DataFrame:

        yearly = (

            df

            .groupby("year")["amount"]

            .sum()

            .reset_index()

            .sort_values("year")

        )

        return yearly

    # =====================================================
    # Top Startups
    # =====================================================

    @staticmethod
    def get_top_startups(
        df: pd.DataFrame,
        top: int = TOP_N
    ) -> pd.DataFrame:

        return (

            df

            .groupby("startup")["amount"]

            .sum()

            .sort_values(

                ascending=False

            )

            .head(top)

            .reset_index()

        )

    # =====================================================
    # Top Investors
    # =====================================================

    @staticmethod
    def get_top_investors(
        df: pd.DataFrame,
        top: int = TOP_N
    ) -> pd.DataFrame:

        return (

            df

            .groupby("investors")["amount"]

            .sum()

            .sort_values(

                ascending=False

            )

            .head(top)

            .reset_index()

        )

    # =====================================================
    # Top Cities
    # =====================================================

    @staticmethod
    def get_top_cities(
        df: pd.DataFrame,
        top: int = TOP_N
    ) -> pd.DataFrame:

        return (

            df

            .groupby("city")["amount"]

            .sum()

            .sort_values(

                ascending=False

            )

            .head(top)

            .reset_index()

        )

    # =====================================================
    # Top Sectors
    # =====================================================

    @staticmethod
    def get_top_sectors(
        df: pd.DataFrame,
        top: int = TOP_N
    ) -> pd.DataFrame:

        return (

            df

            .groupby("vertical")["amount"]

            .sum()

            .sort_values(

                ascending=False

            )

            .head(top)

            .reset_index()

        )

    # =====================================================
    # Funding Round Distribution
    # =====================================================

    @staticmethod
    def get_round_distribution(
        df: pd.DataFrame
    ) -> pd.DataFrame:

        return (

            df

            .groupby("round")["amount"]

            .sum()

            .reset_index()

        )

    # =====================================================
    # Funding Count By Round
    # =====================================================

    @staticmethod
    def get_round_count(
        df: pd.DataFrame
    ) -> pd.DataFrame:

        return (

            df["round"]

            .value_counts()

            .reset_index()

            .rename(

                columns={

                    "index": "round",

                    "round": "count"

                }

            )

        )

    # =====================================================
    # Sector Count
    # =====================================================

    @staticmethod
    def get_sector_count(
        df: pd.DataFrame,
        top: int = TOP_N
    ) -> pd.DataFrame:

        return (

            df["vertical"]

            .value_counts()

            .head(top)

            .reset_index()

            .rename(

                columns={

                    "index": "vertical",

                    "vertical": "count"

                }

            )

        )

    # =====================================================
    # City Count
    # =====================================================

    @staticmethod
    def get_city_count(
        df: pd.DataFrame,
        top: int = TOP_N
    ) -> pd.DataFrame:

        return (

            df["city"]

            .value_counts()

            .head(top)

            .reset_index()

            .rename(

                columns={

                    "index": "city",

                    "city": "count"

                }

            )

        )

    # =====================================================
    # Dataset Summary
    # =====================================================

    @staticmethod
    def get_dataset_summary(
        df: pd.DataFrame
    ) -> dict:

        return {

            "rows": len(df),

            "columns": len(df.columns),

            "missing_values":

                int(

                    df

                    .isna()

                    .sum()

                    .sum()

                )

        }
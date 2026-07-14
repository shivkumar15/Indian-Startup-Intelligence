

from __future__ import annotations

import pandas as pd

from config import (
    STARTUP_NAME_MAPPING,
    CITY_MAPPING,
    UNKNOWN_CITY,
    UNDISCLOSED,
)


class DataCleaner:
    """
    Cleans the dataset before analysis.
    """

    @staticmethod
    def clean(dataframe: pd.DataFrame) -> pd.DataFrame:

        dataframe = dataframe.copy()

        # dataframe = DataCleaner._standardize_column_names(dataframe)

        dataframe = DataCleaner._clean_dates(dataframe)

        dataframe = DataCleaner._clean_amount(dataframe)

        dataframe = DataCleaner._clean_startup_names(dataframe)

        dataframe = DataCleaner._clean_city_names(dataframe)

        dataframe = DataCleaner._clean_text_columns(dataframe)

        dataframe = DataCleaner._remove_duplicates(dataframe)

        dataframe = DataCleaner._create_date_features(dataframe)

        return dataframe

    
    # @staticmethod
    # def _standardize_column_names(
    #     dataframe: pd.DataFrame
    # ) -> pd.DataFrame:

    #     dataframe.columns = (
    #         dataframe.columns
    #         .str.strip()
    #         .str.lower()
    #     )

    #     return dataframe

    
    @staticmethod
    def _clean_dates(
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        dataframe["date"] = pd.to_datetime(
            dataframe["date"],
            format="mixed",
            dayfirst=True,
            errors="coerce"
        )

        return dataframe

    
    @staticmethod
    def _clean_amount(
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        dataframe["amount"] = (
            dataframe["amount"]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.replace("₹", "", regex=False)
            .str.strip()
        )

        dataframe["amount"] = pd.to_numeric(
            dataframe["amount"],
            errors="coerce"
        ).fillna(0)

        return dataframe

    
    @staticmethod
    def _clean_startup_names(
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        dataframe["startup"] = (
            dataframe["startup"]
            .fillna(UNDISCLOSED)
            .astype(str)
            .str.strip()
            .replace(STARTUP_NAME_MAPPING)
        )

        return dataframe

    
    @staticmethod
    def _clean_city_names(
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        dataframe["city"] = (
            dataframe["city"]
            .fillna(UNKNOWN_CITY)
            .astype(str)
            .str.strip()
            .replace(CITY_MAPPING)
        )

        return dataframe

    
    @staticmethod
    def _clean_text_columns(
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        text_columns = [
            "investors",
            "vertical",
            "subvertical",
            "round"
        ]

        for column in text_columns:

            if column in dataframe.columns:

                dataframe[column] = (
                    dataframe[column]
                    .fillna(UNDISCLOSED)
                    .astype(str)
                    .str.strip()
                    .str.replace(" ,", ",", regex=False)
                    .str.replace(", ", ",", regex=False)
                )

        return dataframe

    
    @staticmethod
    def _remove_duplicates(
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        dataframe = dataframe.drop_duplicates(

            subset=[
                "startup",
                "date",
                "amount",
                "round"
            ]

        )

        return dataframe.reset_index(drop=True)

    
    @staticmethod
    def _create_date_features(
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        dataframe["year"] = dataframe["date"].dt.year

        dataframe["month"] = dataframe["date"].dt.month

        dataframe["month_name"] = dataframe["date"].dt.month_name()

        dataframe["quarter"] = dataframe["date"].dt.quarter

        return dataframe
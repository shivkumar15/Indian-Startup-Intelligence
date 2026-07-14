from __future__ import annotations

import pandas as pd

from config import REQUIRED_COLUMNS


class DataValidator:
    """
    Validates dataset structure before cleaning.
    """

    @staticmethod
    def validate(df: pd.DataFrame) -> pd.DataFrame:

        if df.empty:
            raise ValueError("Dataset is empty.")

        missing_columns = [
            column
            for column in REQUIRED_COLUMNS
            if column not in df.columns
        ]

        if missing_columns:

            raise ValueError(
                f"Missing required columns: {missing_columns}"
            )

        return df

    @staticmethod
    def get_dataset_summary(
        df: pd.DataFrame
    ) -> dict:

        return {

            "rows": len(df),

            "columns": len(df.columns),

            "missing_values": int(
                df.isna().sum().sum()
            )

        }
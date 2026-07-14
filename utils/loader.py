

from __future__ import annotations

import pandas as pd
import streamlit as st

from config import DATA_FILE
from utils.validators import DataValidator
from utils.cleaner import DataCleaner


class DataLoader:
    """
    Responsible for loading, validating
    and cleaning the dataset.
    """

    @staticmethod
    @st.cache_data(show_spinner=False)
    def load() -> pd.DataFrame:
        """
        Returns cleaned dataframe.
        """

        dataframe = DataLoader._read_csv()

        # Standardize column names first
        dataframe.columns = (
            dataframe.columns
            .str.strip()
            .str.lower()
        )

        # Validate standardized columns
        dataframe = DataValidator.validate(
            dataframe
        )

        # Clean remaining data
        dataframe = DataCleaner.clean(
            dataframe
        )
        st.session_state["df"] = dataframe

        return dataframe

    
    @staticmethod
    def _read_csv() -> pd.DataFrame:
        """
        Reads the dataset.
        """

        try:

            dataframe = pd.read_csv(
                DATA_FILE,
                low_memory=False
            )

            return dataframe

        except FileNotFoundError:

            raise FileNotFoundError(

                f"""

Dataset not found.

Expected Location

{DATA_FILE}

"""

            )

        except pd.errors.EmptyDataError:

            raise ValueError(

                "Dataset exists but contains no rows."

            )

        except Exception as error:

            raise RuntimeError(

                f"""

Unable to load dataset.

{error}

"""

            )

    
    @staticmethod
    def reload() -> pd.DataFrame:
        """
        Clears Streamlit cache
        and reloads dataset.
        """

        DataLoader.load.clear()

        return DataLoader.load()

    
    @staticmethod
    def get_dataset_summary() -> dict:
        """
        Returns dataset statistics.
        """

        dataframe = DataLoader.load()

        return DataValidator.get_dataset_summary(
            dataframe
        )
"""
====================================================
Indian Startup Intelligence
Configuration File

Author : Shiv Kumar
Version : 2.0
====================================================
"""

from pathlib import Path


# Project Paths


PROJECT_ROOT = Path(__file__).resolve().parent

DATA_DIR = PROJECT_ROOT / "data"

ASSETS_DIR = PROJECT_ROOT / "assets"

PAGES_DIR = PROJECT_ROOT / "pages"

UTILS_DIR = PROJECT_ROOT / "utils"

LLM_DIR = PROJECT_ROOT / "llm"

TEST_DIR = PROJECT_ROOT / "tests"


# Dataset


DATA_FILE = DATA_DIR / "startup_cleaned.csv"


# Application Information


APP_NAME = "Indian Startup Intelligence"

APP_SUBTITLE = (
    "Modern Analytics Platform for India's Startup Ecosystem"
)

APP_VERSION = "2.0"

AUTHOR = "Shiv Kumar"


# Theme


PRIMARY_COLOR = "#2563EB"

SUCCESS_COLOR = "#10B981"

WARNING_COLOR = "#F59E0B"

DANGER_COLOR = "#EF4444"

BACKGROUND_COLOR = "#0F172A"

CARD_COLOR = "#1E293B"

TEXT_COLOR = "#F8FAFC"


# Dashboard Defaults


DEFAULT_YEAR = "All"

DEFAULT_CITY = "All"

DEFAULT_STARTUP = "Select Startup"

DEFAULT_INVESTOR = "Select Investor"

TOP_N = 10

CHART_HEIGHT = 450

TABLE_HEIGHT = 400


# Required Columns


REQUIRED_COLUMNS = [

    "date",

    "startup",

    "vertical",

    "subvertical",

    "city",

    "investors",

    "round",

    "amount"

]


# Missing Value Labels


UNKNOWN_CITY = "Unknown"

UNDISCLOSED = "Undisclosed"


# Startup Name Mapping


STARTUP_NAME_MAPPING = {

    "CarDekho.com": "CarDekho",

    "Flipkart.com": "Flipkart",

    "mamaearth": "MamaEarth",

    "Mamaearth": "MamaEarth",

    "https://www.wealthbucket.in/": "Wealth Bucket"

}


# City Name Mapping


CITY_MAPPING = {

    "Bangalore": "Bengaluru",

    "Bengaluru ": "Bengaluru",

    "Delhi": "New Delhi"

}


# Performance


CACHE_DATA = True

MAX_CACHE_ENTRIES = 5


# Future AI Configuration


ENABLE_AI = False

DEFAULT_LLM = "OpenAI"

ENABLE_RAG = False

VECTOR_STORE = None


# Future Database


DATABASE_ENABLED = False

DATABASE_URI = ""
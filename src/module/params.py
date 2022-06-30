"""
All parameters specific to the application
"""

from os import getenv

PARAMS = {
    "INPUT_LABEL": getenv("INPUT_LABEL", "temperature"),
    "CONDITION": getenv("CONDITION", "No condition"),
    "COMPARE_VALUE": float(getenv("COMPARE_VALUE", 20))
}

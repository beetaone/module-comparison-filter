"""
All constants specific to the application
"""
from app.utils.env import env
from app.utils.floatenv import floatenv


APPLICATION = {
    "INPUT_LABEL": env("INPUT_LABEL", "temperature"),
    "OUTPUT_LABEL": env("OUTPUT_LABEL", "temperature"),
    "OUTPUT_UNIT": env("OUTPUT_UNIT", "Celsius"),
    "CONDITION": env("CONDITION", "<"),
    "COMPARE_VALUE": floatenv("COMPARE_VALUE", 15)
}

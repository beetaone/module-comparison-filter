"""
This file implements module's main logic.
Data processing should happen here.

Edit this file to implement your module.
"""
from .params import PARAMS
from logging import getLogger

log = getLogger("module")

def no_condition(a, b):
    return True

def equal(a, b):
    return a == b

def not_equal(a, b):
    return a != b

def greater(a, b):
    return a > b

def greater_equal(a, b):
    return a >= b

def less(a, b):
    return a < b

def less_equal(a, b):
    return a <= b

comparison_conditions = {
    "No condition": no_condition,
    "(==) equal to": equal,
    "(!=) not equal to": not_equal,
    "(>) greater than": greater,
    "(>=) greater than or equal to": greater_equal,
    "(<) less than": less,
    "(<=) less than or equal to": less_equal
}

def module_main(received_data: any) -> [any, str]:
    """
    Process received data by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        any: Processed data that are ready to be sent to the next module or None if error occurs.
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Processing ...")

    try:
        if comparison_conditions[PARAMS['CONDITION']](received_data[PARAMS['INPUT_LABEL']], PARAMS['COMPARE_VALUE']):
            return received_data, None
        else:
            return None, None

    except Exception as e:
        return None, f"Exception in the module business logic: {e}"

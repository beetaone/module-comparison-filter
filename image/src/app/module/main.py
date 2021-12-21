"""
All logic related to the module's main application
Mostly only this file requires changes
"""
from app.config import APPLICATION

#  Set module settings
__CONDITION__ = APPLICATION['CONDITION']
__COMPARE_VALUE__ = APPLICATION['COMPARE_VALUE']
__INPUT_LABEL__ = APPLICATION['INPUT_LABEL']

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

def module_main(parsed_data):
    """implement module logic here

    Args:
        parsed_data ([JSON Object]): [The output of data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    try:
        if comparison_conditions[__CONDITION__](parsed_data[__INPUT_LABEL__], __COMPARE_VALUE__):
            return parsed_data[__INPUT_LABEL__], None
        else: return None, None
    except Exception:
        return None, "Unable to perform the module logic"

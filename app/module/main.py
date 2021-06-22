"""
All logic related to the module's main application
Mostly only this file requires changes
"""
from app.config import APPLICATION

#  Set module settings
__CONDITION__ = APPLICATION['CONDITION']
__COMPARE_VALUE__ = APPLICATION['COMPARE_VALUE']

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
    "==": equal,
    "!=": not_equal,
    ">": greater,
    ">=": greater_equal,
    "<": less,
    "<=": less_equal
}

def module_main(parsed_data):
    """implement module logic here

    Args:
        parsed_data ([JSON Object]): [The output of data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    try:
        if comparison_conditions[__CONDITION__](parsed_data, __COMPARE_VALUE__):
            return parsed_data, None
        else: return None, None
    except Exception:
        return None, "Unable to perform the module logic"

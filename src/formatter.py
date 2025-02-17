# src/formatter.py
# Formatting Functions

def convert_to_snake_case(Pascal_or_camelCased_string):
    """
    Converts a Pascal case or camelCase string to snake_case.
    
    Args:
        Pascal_or_camelCased_string: single string
        
    Returns:
        A string converted to snake_case.
    
    """
    snake_cased_string = ''

    for char in Pascal_or_camelCased_string:
        
        if char.isupper():
            snake_cased_string += '_' + char.lower()
        
        else:
            snake_cased_string += char

    return snake_cased_string.strip('_')


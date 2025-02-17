# Formatting Functions

def convert_to_snake_case(Pascal_or_camelCased_string):
    """
    Convert the column names of a DataFrame to snake_case.
    
    Args:
        df (pd.DataFrame): Input DataFrame with original column names.
        
    Returns:
        pd.DataFrame: DataFrame with column names in snake_case.
    
    """
    snake_cased_string = ''

    for char in Pascal_or_camelCased_string:
        
        if char.isupper():
            snake_cased_string += '_' + char.lower()
        
        else:
            snake_cased_string += char

        return snake_cased_string.strip('_')
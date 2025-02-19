# src/formatter.py
# Cleaning and Formatting Functions

def drop_columns(df):
    print(f'\nSelect an option to drop unnecessary columns: \n')
    print(f'1. Drop default columns.')
    print(f'2. Select from a list.')

    while True: 
        choice = input(f'\nEnter your choice (1 or 2): ').strip()

        if choice in ['1','2']:
            break
        else:
            print("\nInvalid choice. Please enter 1 or 2.")

    if choice == '1':
        default = ['volume','unadjusted_volume','change','change_percent','vwap','label','change_over_time']
        return df.drop(columns=default)

    elif choice == '2':
        print('\nSelect columns to drop from the following list: ')
        print(list(df.columns)[1:-1])
        
        while True:
            drop_cols = input(f'\nEnter columns to drop, separated by commas: ').split(",")
            drop_cols = [col.strip().lower() for col in drop_cols]

            if all(col in list(df.columns)[1:-1] for col in drop_cols):
                break
            else:
                print("Please select columns from list:")

        return df.drop(columns=drop_cols)

    print('\nRemaining columns: ')
    print(list(df.columns))

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


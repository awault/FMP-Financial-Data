# Use this file to test operation of functions in terminal

# test.py
import sys
import os

# Add the 'src' directory to the system path to import from it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Import the function
from formatter import convert_to_snake_case

# Test cases
def test_convert_to_snake_case():
    assert convert_to_snake_case('PascalCase') == 'pascal_case', 'Test 1 Failed'
    assert convert_to_snake_case('camelCase') == 'camel_case', 'Test 2 Failed'
    assert convert_to_snake_case('snake_case') == 'snake_case', 'Test 3 Failed'
    assert convert_to_snake_case('Single') == 'single', 'Test 4 Failed'
    assert convert_to_snake_case('AnotherTestString') == 'another_test_string', 'Test 5 Failed'
    
    print('All tests passed!')

# Run the test
test_convert_to_snake_case()

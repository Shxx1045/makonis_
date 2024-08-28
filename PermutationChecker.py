from collections import Counter

def validate_input(string):
    """
    Validates the input string. It checks if the string is a valid string type,
    contains only alphabetic characters (or is empty), and converts it to 
    lowercase for case-insensitive comparison.
    """
    # Ensure the input is a string
    if not isinstance(string, str):
        raise ValueError("Input must be a string.")
    
    # Ensure the string contains only alphabetic characters or is empty
    if string and not string.replace(" ", "").isalpha():
        raise ValueError(f"String contains invalid characters, it must be only alphabetic: {string}")
    
    # Convert the string to lowercase and remove spaces
    return string.lower().replace(" ", "")

def permutations_check(string1, string2):
    try:
        # Validate both input strings to ensure they are preprocessed
        string1 = validate_input(string1)
        string2 = validate_input(string2)
        
        # If lengths are not the same, they can't be permutations
        if len(string1) != len(string2):
            return False
        
        # Use a frequency counter to compare characters in both strings
        return Counter(string1) == Counter(string2)
    
    except ValueError as e:
        print(f"Error: {e}")
        return False



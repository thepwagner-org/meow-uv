# Valid cat sounds in different languages
valid_cat_sounds = frozenset([
    "meow",  # English
    "nyaa",  # Japanese
    "nyan",  # Japanese
    "yaong", # Korean
    "miao",  # Chinese
    "miau",  # Spanish/German
    "miaou", # French
    "myau",  # Russian
])

def is_meow(text: str) -> bool:
    """
    Checks if a given string is a valid cat sound
    
    Args:
        text: The string to check
        
    Returns:
        bool: True if the string is a valid cat sound, false otherwise
    """
    if not text:
        return False
    
    return text.lower() in valid_cat_sounds 
# Created on: 05-29-2024

def get_filename_extension(filename):
    """
    Finds the file extension for a given filename string.

    This program used str.rfind(), lambda functions, dictionaries, and string slicing.

    Parameters:
        filename (str): A filename.

    Returns:
        str: The file extension description. If the extension is not in the dictionary, returns "Unknown".

    Examples:
    >>> get_filename_extension("hello_world.txt")
    'Text'
    >>> get_filename_extension("business_pitch.ppt")
    'Unknown'
    """

    char_index = filename.rfind(".")
    get_extension = lambda ext: {
        ".txt": "Text",
        ".docx": "Word",
        ".java": "Java",
        ".py": "Python",
    }.get(ext, "Unknown")
    
    return get_extension(filename[char_index:])

# Created on: 06-01-2024

def get_file_paths_from_dict(directory, current_path=""):
    """
    Recursively collects all file paths from a nested directory structure.

    This program used recursion and the str.rstrip() method.

    Parameters:
        directory (dict): Nested dictionary containing a directory structure.
            Keys are folder names. Values can be either filenames, nested dictionaries, or None.

        current_path (str): Current path in the traversed directory. Defaults to "".

    Returns:
        list: List of all file paths from the nested directory.

    Examples:
    >>> get_filename_extension({
            "Photos": summer.png,
            "Documents": { "resume.doc": None, "letter.doc": None,},
        })
    ['/Photos/summer.png', '/Documents/resume.doc', '/Documents/letter.doc']
    """

    paths = []

    for key, value in directory.items():
        new_path = f"{current_path}/{key}"

        if not isinstance(value, dict):
            paths.append(f"{new_path}/{value}")
        else:
            paths.extend(get_file_paths_from_dict(value, new_path))

    paths = [path.rstrip("/None") for path in paths]

    return paths

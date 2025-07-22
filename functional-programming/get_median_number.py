# Created on: 05-29-2024

def get_median_number(unsorted_numbers):
    '''
    This program calculates the median number from an unsorted list of numbers.

    This program used modulus, floor division, string slicing, and sorted(). The sorted() method acts on iterables.

    Parameters:
        unsorted_numbers (list): A list of numbers.

    Returns:
        float or int: The median of the list. If the list is empty, returns None.

    Examples:
    >>> get_median_number([10, 2, 8, 4, 6, 12])
    7.0
    >>> get_median_number([15, 3, 7, 9, 11])
    9
    '''

    if len(unsorted_numbers) == 0:
        return None

    is_length = len(unsorted_numbers)
    is_odd = is_length % 2 != 0
    i = is_length // 2
    is_sorted = sorted(unsorted_numbers)
    
    return is_sorted[i] if is_odd else sum(is_sorted[i-1:i+1]) / 2
